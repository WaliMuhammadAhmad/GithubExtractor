from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from services.getRepos.fetch import get_repo_details
from typing import List, Optional, Union, Dict, Any
import os

load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/repos": {"origins": os.getenv("API_ORIGIN") }})

# Directory to store generated files
UPLOAD_FOLDER = 'downloads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/repos', methods=['POST'])
def repos() -> tuple[Dict[str, str], int]:
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    req: Dict[str, Any] = request.get_json()
    if not req:
        return jsonify({"error": "No data provided"}), 400
    
    print(req)
    
    try:
        # Required field
        language: str = req['language']
        sort: str = req.get('sort')  
        order: str = req.get('order')

        # Optional fields with type hints
        name: Optional[str] = req.get('name')  # string or None
        description: Optional[str] = req.get('description')  # string or None
        readme: Optional[str] = req.get('readme')  # string or None
        owner: Optional[str] = req.get('owner')  # string or None
        user: Optional[str] = req.get('user')  # string or None
        org: Optional[str] = req.get('org')  # string or None
        min_size: Optional[int] = req.get('min_size')  # number (int) or None
        max_size: Optional[int] = req.get('max_size')  # number (int) or None
        followers: Optional[int] = req.get('followers')  # number (int) or None
        min_forks: Optional[int] = req.get('min_forks')  # number (int) or None
        max_forks: Optional[int] = req.get('max_forks')  # number (int) or None
        fork: Optional[str] = req.get('fork')  # "true", "only", or None
        min_stars: Optional[int] = req.get('min_stars')  # number (int) or None
        max_stars: Optional[int] = req.get('max_stars')  # number (int) or None
        created: Optional[str] = req.get('created')  # date string (YYYY-MM-DD) or None
        pushed: Optional[str] = req.get('pushed')  # date string (YYYY-MM-DD) or None
        topic: List[str] = req.get('topic', [])  # list of strings, default empty list
        topics: Optional[int] = req.get('topics')  # number (int) or None
        min_topics: int = len(topic) if topic is not None else 0  # number (count of topics)
        license: Optional[str] = req.get('license')  # string or None
        mirror: Optional[bool] = req.get('mirror')  # True, False, or None
        template: Optional[bool] = req.get('template')  # True, False, or None
        archived: Optional[bool] = req.get('archived')  # True, False, or None
        good_first_issues: Optional[int] = req.get('good_first_issues')  # number (int) or None
        help_wanted_issues: Optional[int] = req.get('help_wanted_issues')  # number (int) or None
        sponsorable: Optional[str] = req.get('sponsorable')  # string or None (e.g., "true")
        funding: Optional[str] = req.get('funding')  # string or None (e.g., "true")

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Invalid request data: {str(e)}"}), 400
    
    # Build the query dynamically
    query_parts: List[str] = [f"language:{language}"]
    if name:
        query_parts.append(f"{name} in:name")
    if description:
        query_parts.append(f"{description} in:description")
    if readme:
        query_parts.append(f"{readme} in:readme")
    if owner and name:
        query_parts.append(f"repo:{owner}/{name}")
    if user:
        query_parts.append(f"user:{user}")
    if org:
        query_parts.append(f"org:{org}")
    if min_size is not None and max_size is not None:
        size_range = f"size:{min_size}..{max_size}".strip(':')
        query_parts.append(size_range)
    else :
        if min_size is not None:
            query_parts.append(f"size:>={min_size}")
        if max_size is not None:
            query_parts.append(f"size:<={max_size}")
    if followers is not None:
        query_parts.append(f"followers:>={followers}")
    if min_forks is not None and max_forks is not None:
        fork_range = f"forks:{min_forks}..{max_forks}".strip(':')
        query_parts.append(fork_range)
    else:
        if min_forks is not None:
            query_parts.append(f"forks:>={min_forks}")
        if max_forks is not None:
            query_parts.append(f"forks:<={max_forks}")
    if fork:
        query_parts.append(f"fork:{fork}")
    if min_stars is not None and max_stars is not None:
        star_range = f"stars:{min_stars}..{max_stars}".strip(':')
        query_parts.append(star_range)
    else:
        if min_stars is not None:
            query_parts.append(f"stars:>={min_stars}")
        if max_stars is not None:
            query_parts.append(f"stars:<={max_stars}")
    if created:
        query_parts.append(f"created:>={created}")
    if pushed:
        query_parts.append(f"pushed:>={pushed}")
    if topic:
        query_parts.extend([f"topic:{t}" for t in topic])
    if topics is not None:
        query_parts.append(f"topics:{topics}")
    if min_topics is not None:
        query_parts.append(f"topics:>={min_topics}")
    if license and license.lower() != "none":
        query_parts.append(f"license:{license}")
    if mirror is not None:
        query_parts.append(f"mirror:{str(mirror).lower()}")
    if template is not None:
        query_parts.append(f"template:{str(template).lower()}")
    if archived is not None:
        query_parts.append(f"archived:{str(archived).lower()}")
    if good_first_issues is not None:
        query_parts.append(f"good-first-issues:>{good_first_issues}")
    if help_wanted_issues is not None:
        query_parts.append(f"help-wanted-issues:>{help_wanted_issues}")
    if sponsorable:
        query_parts.append("is:sponsorable")
    if funding:
        query_parts.append("has:funding-file")

    query: str = " ".join(query_parts)
    
    try:
        file_path = get_repo_details(lang=language,query=query, sort=sort, order=order, output_dir=UPLOAD_FOLDER)
        if not file_path or not os.path.exists(file_path):
            return jsonify({"error": "Failed to generate file"}), 500
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500
    
    filename = os.path.basename(file_path)
    download_link = f"http://{request.host}/download/{filename}"
    return jsonify({"message": "Received", "download_link": download_link}), 200

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)