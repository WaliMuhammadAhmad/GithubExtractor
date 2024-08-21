# Notebooks which uses method2test dataset

This dir contains notebooks for extracting and preparing the dataset from the [methods2test](https://github.com/microsoft/methods2test) repository for the use with Deepseek and Llama models. 

## dir Structure

```plaintext
method2test/
├── Prep4Deepseek/
│   ├── Eval4Deepseek_Coder.ipynb
│   ├── Test4Deepseek_Coder.ipynb
│   └── Train4Deepseek_Coder.ipynb
├── Prep4Llama/
│   ├── Prep4LlamaModels.py
│   ├── Eval4llama.ipynb
│   ├── Test4Llama.ipynb
│   └── Train4Llama.ipynb
└── Method2Test[Extract_Dataset].ipynb
```

## Contents

- `Method2Test[Extract_Dataset].ipynb` - Jupyter notebook that clones the `methods2test` repository, extracts the required `.tar.bz2` files, counts the JSON files, and compresses the dataset into a ZIP file.
- `Prep4Deepseek` - dir for Notebook for Deepseek to prepare the dataset specifically for use with the Deepseek models.
- `Prep4Llama` - dir for Notebook for Llama to prepare the dataset specifically for use with the Llama model.

## Overview

### Method2Test[Extract_Dataset].ipynb

This notebook is responsible for the following tasks:

1. **Cloning the Repository:**
   - Clones the `methods2test` repository from GitHub.
   - Uses `git lfs` to pull large files required for the dataset.

2. **Extracting Files:**
   - Extracts `.tar.bz2` files from the `corpus/json` directory.
   - Counts the number of `.json` files within the extracted directories.

3. **Zipping the Dataset:**
   - Compresses the extracted dataset into a ZIP file for easy distribution or further processing.

4. **Releasing Storage:**
   - Removes the cloned repository and extracted files to free up storage.

### Prep4Deepseek
This is a sub-dir which contains notebook for preparing the dataset acording to deepseek models input format. The original dataset are courps in this format: 

```plaintext
FM: focal method
FM_FC: focal method + focal class name
FM_FC_CO: focal method + focal class name + constructor signatures
FM_FC_MS: focal method + focal class name + constructor signatures + public method signatures
FM_FC_MS_FF: focal method + focal class name + constructor signatures + public method signatures + public fields
```

Deepseek models takes input in a specific format before tokenization. A snap short of the deepseek model input format is:

```JSON
{
    "instruction": "Generate a unit test case for the following Java method: TimestampsParser { public static TimestampSet parseTimestampSet(String input, DateTimeZone timeZone) throws IllegalArgumentException { if (input == null) { return null; } if (input.equalsIgnoreCase(EMPTY_VALUE)) { return new TimestampSet(); } ArrayList<String> values = new ArrayList<String>(); try { StringReader reader = new StringReader(input + ' '); int r; char c; while ((r = reader.read()) != -1) { c = (char) r; switch (c) { case DYNAMIC_TYPE_LEFT_BOUND: case DYNAMIC_TYPE_RIGHT_BOUND: case RIGHT_BOUND_SQUARE_BRACKET: case RIGHT_BOUND_BRACKET: case LEFT_BOUND_BRACKET: case LEFT_BOUND_SQUARE_BRACKET: case ' ': case '\\t': case '\\r': case '\\n': case COMMA: break; case '\"': case '\\'': values.add(FormattingAndParsingUtils.parseLiteral(reader, c)); break; default: reader.skip(-1); values.add(FormattingAndParsingUtils.parseValue(reader)); } } } catch (IOException ex) { throw new RuntimeException(\"Unexpected expection while parsing timestamps\", ex); } TimestampSet result = new TimestampSet(values.size()); for (String value : values) { result.add(FormattingAndParsingUtils.parseDateTimeOrTimestamp(value, timeZone)); } return result; }  static TimestampSet parseTimestampSet(String input, DateTimeZone timeZone); static TimestampSet parseTimestampSet(String input); static TimestampMap<T> parseTimestampMap(Class<T> typeClass, String input, DateTimeZone timeZone); static TimestampMap<T> parseTimestampMap(Class<T> typeClass, String input);  }",
    "output": "The unit test case for the given Java method is: @Test(expectedExceptions = IllegalArgumentException.class) public void testParseTimestampSetBadDateFormat1() { TimestampsParser.parseTimestampSet(\"[2015-13-01, 2015-01-31]\"); }"
}
```

#### Notebook Explanation
- **Purpose**: Prepares the dataset for train,test,eval by extracting JSON data from `.tar.bz2` files, formatting it according to deepseek models input, and converting it into JSON files.
- **Key Steps**:
   - Extracts data from compressed files.
   - Process the data inside the JSON courps files as deepseek model input format.
   - Export the JSON files.
   - Logs processes and handles errors.
   - Counts files to ensure data consistency.
   - Pushes processed data to a Hugging Face repository.

### Prep4Llama
This is a sub-dir which contains notebook for preparing the dataset acording to Llama models input format. The original dataset are courps in this format: 

```plaintext
FM: focal method
FM_FC: focal method + focal class name
FM_FC_CO: focal method + focal class name + constructor signatures
FM_FC_MS: focal method + focal class name + constructor signatures + public method signatures
FM_FC_MS_FF: focal method + focal class name + constructor signatures + public method signatures + public fields
```

Llama models takes input in a specific format before tokenization. A snap short of the Llama model input format is:

```csv
"<s> <<SYS>> Generate Unit Test Case for this Unit <</SYS>> [INST] NetUtil { public static byte[] download(String url) throws IOException { return download(new URL(url)); } private  NetUtil(); static boolean checkPort(String host, int port); static byte[] download(String url); static void download(String url, File file); static byte[] download(URL url); static void download(URL url, File file); static Optional<String> serviceName(int port);  } [/INST] @Test @DisplayName(""Download a small file to the filesystem"") void download_2(@Tempdir Path temp) throws IOException { download(""https: temp.resolve(""test.txt"").toFile()); assertTrue(Files.exists(temp.resolve(""test.txt""))); assertTrue(Files.size(temp.resolve(""test.txt"")) > 0); } </s>"
```

#### Notebook Explanation
- **Purpose**: Prepares the dataset for train,test,eval by extracting JSON data from `.tar.bz2` files, formatting it according to Llama models input, and converting it into JSON files.
- **Key Steps**:
   - Extracts data from compressed files.
   - Process the data inside the JSON courps files as Llama model input format.
   - Export the CSV files.
   - Logs processes and handles errors.
   - Counts files to ensure data consistency.
   - Pushes processed data to a Hugging Face repository.