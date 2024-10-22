import os
import subprocess
import platform

# Function to compile Java file
def compile_java(java_file, classpath=""):
    # Create the compile command
    if classpath:
        compile_cmd = ['javac', '-d', 'bin', '-cp', classpath, java_file]
    else:
        compile_cmd = ['javac', '-d', 'bin', java_file]
    
    # Run the compile command
    process = subprocess.run(compile_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.returncode != 0:
        print(f"Compilation Error in {java_file}: ", process.stderr.decode())
        return False
    return True

# Function to run JUnit test
def run_junit_test(test_class_file):
    # Path to the JAR files in the `lib/` folder
    junit_jar = os.path.join('lib', 'junit-4.13.2.jar')
    hamcrest_jar = os.path.join('lib', 'hamcrest-core-1.3.jar')

    # Determine the classpath separator based on the operating system
    classpath_separator = ';' if platform.system() == 'Windows' else ':'

    # Java command to run the JUnit test (use correct classpath separator)
    run_cmd = [
        'java', '-cp', f'bin{classpath_separator}{junit_jar}{classpath_separator}{hamcrest_jar}',
        'org.junit.runner.JUnitCore', test_class_file
    ]

    # Run the JUnit test
    process = subprocess.run(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Handle the output
    if process.returncode != 0:
        print(f"Test Execution Error in {test_class_file}: ", process.stderr.decode())
    else:
        print("Test Output: ", process.stdout.decode())
    
    return process.returncode

# Main execution
if __name__ == "__main__":
    # Create a bin folder to store the compiled class files
    if not os.path.exists('bin'):
        os.makedirs('bin')

    # Classpath for compilation (JAR files and bin directory)
    junit_jar = os.path.join('lib', 'junit-4.13.2.jar')
    hamcrest_jar = os.path.join('lib', 'hamcrest-core-1.3.jar')
    classpath = f'bin{os.pathsep}{junit_jar}{os.pathsep}{hamcrest_jar}'

    # Compile the main Java code
    main_java_file = 'src/main/HelloWorld.java'
    if not compile_java(main_java_file, classpath):
        exit(1)  # Exit if compilation fails

    # Compile the test Java code with the classpath including the compiled main class
    test_java_file = 'src/test/HelloWorldTest.java'
    if not compile_java(test_java_file, classpath):
        exit(1)  # Exit if compilation fails

    # Run the test case
    run_junit_test('HelloWorldTest')
