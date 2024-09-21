# Dataset

This dir contains dataset extracted from **Github Public Java Repositories** using [Scraper](../Scraper/) and [Scraper-v1](../Scraper-v1.0/). The major dataset gathered is from prior Scrapper. Us `git lfs` to fetch these files. Each of these folder contains  `.zip` files, which contais JSON files of data instance. The `corpus` and `raw` are pushed on **Huggingface**.

## dir Structure

```plaintext
dataset/
├── corpus/
│   ├── eval.zip
│   ├── test.zip
│   └── test.zip
├── dataset-v1.0/
│   └── dataset.zip
└── corpus/
    ├── eval.zip
    ├── test.zip
    └── test.zip
```

## Contents

- `dataset-v1` - dir contains the dataset gathered from the [Scraper-v1](../Scraper-v1.0/).
- `raw` - dir contains the the dataset gathered from the [Scraper](../Scraper/) in the raw form.
- `corpus` - dir contains the actual dataset.
  
## Overview

### corpus/*.zip

The corpus dir containes the actual dataset. The dataset is split into *train,test,eval* already where each zip file contains the split name. **60% data is in train.zip and the other test and eval.zip have 20% 20% data.** This is filtered result from the *raw* dataset, used to get the useful dataset from the raw dataset. This dataset is further transformed and then pushed to huggingface, where it is used for fine-tuning various models. A snapshot of the datset instance is here:

```JSON
{
    "focal_method": "public Response filter(FilterableRequestSpecification requestSpec, FilterableResponseSpecification responseSpec, FilterContext ctx) {\n\n        final CookieOrigin cookieOrigin = cookieOriginFromUri(requestSpec.getURI());\n        for (Cookie cookie : cookieStore.getCookies()) {\n            if (cookieSpec.match(cookie, cookieOrigin) && allowMultipleCookiesWithTheSameNameOrCookieNotPreviouslyDefined(requestSpec, cookie)) {\n                requestSpec.cookie(cookie.getName(), cookie.getValue());\n            }\n        }\n\n        final Response response = ctx.next(requestSpec, responseSpec);\n\n        List<Cookie> responseCookies = extractResponseCookies(response, cookieOrigin);\n        cookieStore.addCookies(responseCookies.toArray(new Cookie[0]));\n        return response;\n    }",
    "test_case": "@Test\n    public void doesntAddCookiesToNonMatchingUrlRequest() {\n\n        FilterableRequestSpecification reqNonMatchingDomain =\n                (FilterableRequestSpecification) given().with().baseUri(\"https://someother.com/somepath\");\n\n        cookieFilter.filter(reqOriginDomain, response, testFilterContext);\n        cookieFilter.filter(reqNonMatchingDomain, response, testFilterContext);\n\n        assertThat(reqNonMatchingDomain.getCookies().size(), Matchers.is(0));\n    }"
}
```

### dataset-v1.0\dataset.zip

The dataset-v1.0 dir containes the dataset gathered using the first Scrapper. The dataset isnt useful but it's wasted many time and resources so this is for showcase this. 

### raw/*.zip

This raw dir containe the raw dataset. This is also split in *train,test,eval* already where each zip file contains the split name. **60% data is in train.zip and the other test and eval.zip have 20% 20% data.** The raw dataset is the actaul output of the Scrapper. A snapshow of the data instance is here:

```JSON
{
    "test_class": {
        "identifier": "CollectionUtilsTest",
        "superclass": "",
        "interfaces": "",
        "fields": [],
        "file": "yudao-framework/yudao-common/src/test/java/cn/iocoder/yudao/framework/common/util/collection/CollectionUtilsTest.java"
    },
    "test_case": {
        "identifier": "testDiffList",
        "parameters": "()",
        "modifiers": "@Test public",
        "return": "void",
        "body": "@Test\n    public void testDiffList() {\n        // \u51c6\u5907\u53c2\u6570\n        Collection<Dog> oldList = Arrays.asList(\n                new Dog(1, \"\u82b1\u82b1\", \"hh\"),\n                new Dog(2, \"\u65fa\u8d22\", \"wc\")\n        );\n        Collection<Dog> newList = Arrays.asList(\n                new Dog(null, \"\u82b1\u82b12\", \"hh\"),\n                new Dog(null, \"\u5c0f\u767d\", \"xb\")\n        );\n        BiFunction<Dog, Dog, Boolean> sameFunc = (oldObj, newObj) -> {\n            boolean same = oldObj.getCode().equals(newObj.getCode());\n            // \u5982\u679c\u76f8\u7b49\u7684\u60c5\u51b5\u4e0b\uff0c\u9700\u8981\u8bbe\u7f6e\u4e0b id\uff0c\u540e\u7eed\u597d\u66f4\u65b0\n            if (same) {\n                newObj.setId(oldObj.getId());\n            }\n            return same;\n        };\n\n        // \u8c03\u7528\n        List<List<Dog>> result = CollectionUtils.diffList(oldList, newList, sameFunc);\n        // \u65ad\u8a00\n        assertEquals(result.size(), 3);\n        // \u65ad\u8a00 create\n        assertEquals(result.get(0).size(), 1);\n        assertEquals(result.get(0).get(0), new Dog(null, \"\u5c0f\u767d\", \"xb\"));\n        // \u65ad\u8a00 update\n        assertEquals(result.get(1).size(), 1);\n        assertEquals(result.get(1).get(0), new Dog(1, \"\u82b1\u82b12\", \"hh\"));\n        // \u65ad\u8a00 delete\n        assertEquals(result.get(2).size(), 1);\n        assertEquals(result.get(2).get(0), new Dog(2, \"\u65fa\u8d22\", \"wc\"));\n    }",
        "signature": "void testDiffList()",
        "full_signature": "@Test public void testDiffList()",
        "class_method_signature": "CollectionUtilsTest.testDiffList()",
        "testcase": true,
        "constructor": false,
        "invocations": [
            "asList",
            "asList",
            "equals",
            "getCode",
            "getCode",
            "setId",
            "getId",
            "diffList",
            "assertEquals",
            "size",
            "assertEquals",
            "size",
            "get",
            "assertEquals",
            "get",
            "get",
            "assertEquals",
            "size",
            "get",
            "assertEquals",
            "get",
            "get",
            "assertEquals",
            "size",
            "get",
            "assertEquals",
            "get",
            "get"
        ]
    },
    "focal_class": {
        "identifier": "CollectionUtils",
        "superclass": "",
        "interfaces": "",
        "fields": [],
        "methods": [
            {
                "identifier": "containsAny",
                "parameters": "(Object source, Object... targets)",
                "modifiers": "public static",
                "return": "boolean",
                "signature": "boolean containsAny(Object source, Object... targets)",
                "full_signature": "public static boolean containsAny(Object source, Object... targets)",
                "class_method_signature": "CollectionUtils.containsAny(Object source, Object... targets)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "isAnyEmpty",
                "parameters": "(Collection<?>... collections)",
                "modifiers": "public static",
                "return": "boolean",
                "signature": "boolean isAnyEmpty(Collection<?>... collections)",
                "full_signature": "public static boolean isAnyEmpty(Collection<?>... collections)",
                "class_method_signature": "CollectionUtils.isAnyEmpty(Collection<?>... collections)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "anyMatch",
                "parameters": "(Collection<T> from, Predicate<T> predicate)",
                "modifiers": "public static",
                "return": "boolean",
                "signature": "boolean anyMatch(Collection<T> from, Predicate<T> predicate)",
                "full_signature": "public static boolean anyMatch(Collection<T> from, Predicate<T> predicate)",
                "class_method_signature": "CollectionUtils.anyMatch(Collection<T> from, Predicate<T> predicate)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "filterList",
                "parameters": "(Collection<T> from, Predicate<T> predicate)",
                "modifiers": "public static",
                "return": "List<T>",
                "signature": "List<T> filterList(Collection<T> from, Predicate<T> predicate)",
                "full_signature": "public static List<T> filterList(Collection<T> from, Predicate<T> predicate)",
                "class_method_signature": "CollectionUtils.filterList(Collection<T> from, Predicate<T> predicate)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "distinct",
                "parameters": "(Collection<T> from, Function<T, R> keyMapper)",
                "modifiers": "public static",
                "return": "List<T>",
                "signature": "List<T> distinct(Collection<T> from, Function<T, R> keyMapper)",
                "full_signature": "public static List<T> distinct(Collection<T> from, Function<T, R> keyMapper)",
                "class_method_signature": "CollectionUtils.distinct(Collection<T> from, Function<T, R> keyMapper)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "distinct",
                "parameters": "(Collection<T> from, Function<T, R> keyMapper, BinaryOperator<T> cover)",
                "modifiers": "public static",
                "return": "List<T>",
                "signature": "List<T> distinct(Collection<T> from, Function<T, R> keyMapper, BinaryOperator<T> cover)",
                "full_signature": "public static List<T> distinct(Collection<T> from, Function<T, R> keyMapper, BinaryOperator<T> cover)",
                "class_method_signature": "CollectionUtils.distinct(Collection<T> from, Function<T, R> keyMapper, BinaryOperator<T> cover)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertList",
                "parameters": "(T[] from, Function<T, U> func)",
                "modifiers": "public static",
                "return": "List<U>",
                "signature": "List<U> convertList(T[] from, Function<T, U> func)",
                "full_signature": "public static List<U> convertList(T[] from, Function<T, U> func)",
                "class_method_signature": "CollectionUtils.convertList(T[] from, Function<T, U> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertList",
                "parameters": "(Collection<T> from, Function<T, U> func)",
                "modifiers": "public static",
                "return": "List<U>",
                "signature": "List<U> convertList(Collection<T> from, Function<T, U> func)",
                "full_signature": "public static List<U> convertList(Collection<T> from, Function<T, U> func)",
                "class_method_signature": "CollectionUtils.convertList(Collection<T> from, Function<T, U> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertList",
                "parameters": "(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "modifiers": "public static",
                "return": "List<U>",
                "signature": "List<U> convertList(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "full_signature": "public static List<U> convertList(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "class_method_signature": "CollectionUtils.convertList(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertListByFlatMap",
                "parameters": "(Collection<T> from,\n                                                      Function<T, ? extends Stream<? extends U>> func)",
                "modifiers": "public static",
                "return": "List<U>",
                "signature": "List<U> convertListByFlatMap(Collection<T> from,\n                                                      Function<T, ? extends Stream<? extends U>> func)",
                "full_signature": "public static List<U> convertListByFlatMap(Collection<T> from,\n                                                      Function<T, ? extends Stream<? extends U>> func)",
                "class_method_signature": "CollectionUtils.convertListByFlatMap(Collection<T> from,\n                                                      Function<T, ? extends Stream<? extends U>> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertListByFlatMap",
                "parameters": "(Collection<T> from,\n                                                         Function<? super T, ? extends U> mapper,\n                                                         Function<U, ? extends Stream<? extends R>> func)",
                "modifiers": "public static",
                "return": "List<R>",
                "signature": "List<R> convertListByFlatMap(Collection<T> from,\n                                                         Function<? super T, ? extends U> mapper,\n                                                         Function<U, ? extends Stream<? extends R>> func)",
                "full_signature": "public static List<R> convertListByFlatMap(Collection<T> from,\n                                                         Function<? super T, ? extends U> mapper,\n                                                         Function<U, ? extends Stream<? extends R>> func)",
                "class_method_signature": "CollectionUtils.convertListByFlatMap(Collection<T> from,\n                                                         Function<? super T, ? extends U> mapper,\n                                                         Function<U, ? extends Stream<? extends R>> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "mergeValuesFromMap",
                "parameters": "(Map<K, List<V>> map)",
                "modifiers": "public static",
                "return": "List<V>",
                "signature": "List<V> mergeValuesFromMap(Map<K, List<V>> map)",
                "full_signature": "public static List<V> mergeValuesFromMap(Map<K, List<V>> map)",
                "class_method_signature": "CollectionUtils.mergeValuesFromMap(Map<K, List<V>> map)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertSet",
                "parameters": "(Collection<T> from)",
                "modifiers": "public static",
                "return": "Set<T>",
                "signature": "Set<T> convertSet(Collection<T> from)",
                "full_signature": "public static Set<T> convertSet(Collection<T> from)",
                "class_method_signature": "CollectionUtils.convertSet(Collection<T> from)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertSet",
                "parameters": "(Collection<T> from, Function<T, U> func)",
                "modifiers": "public static",
                "return": "Set<U>",
                "signature": "Set<U> convertSet(Collection<T> from, Function<T, U> func)",
                "full_signature": "public static Set<U> convertSet(Collection<T> from, Function<T, U> func)",
                "class_method_signature": "CollectionUtils.convertSet(Collection<T> from, Function<T, U> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertSet",
                "parameters": "(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "modifiers": "public static",
                "return": "Set<U>",
                "signature": "Set<U> convertSet(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "full_signature": "public static Set<U> convertSet(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "class_method_signature": "CollectionUtils.convertSet(Collection<T> from, Function<T, U> func, Predicate<T> filter)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMapByFilter",
                "parameters": "(Collection<T> from, Predicate<T> filter, Function<T, K> keyFunc)",
                "modifiers": "public static",
                "return": "Map<K, T>",
                "signature": "Map<K, T> convertMapByFilter(Collection<T> from, Predicate<T> filter, Function<T, K> keyFunc)",
                "full_signature": "public static Map<K, T> convertMapByFilter(Collection<T> from, Predicate<T> filter, Function<T, K> keyFunc)",
                "class_method_signature": "CollectionUtils.convertMapByFilter(Collection<T> from, Predicate<T> filter, Function<T, K> keyFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertSetByFlatMap",
                "parameters": "(Collection<T> from,\n                                                    Function<T, ? extends Stream<? extends U>> func)",
                "modifiers": "public static",
                "return": "Set<U>",
                "signature": "Set<U> convertSetByFlatMap(Collection<T> from,\n                                                    Function<T, ? extends Stream<? extends U>> func)",
                "full_signature": "public static Set<U> convertSetByFlatMap(Collection<T> from,\n                                                    Function<T, ? extends Stream<? extends U>> func)",
                "class_method_signature": "CollectionUtils.convertSetByFlatMap(Collection<T> from,\n                                                    Function<T, ? extends Stream<? extends U>> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertSetByFlatMap",
                "parameters": "(Collection<T> from,\n                                                       Function<? super T, ? extends U> mapper,\n                                                       Function<U, ? extends Stream<? extends R>> func)",
                "modifiers": "public static",
                "return": "Set<R>",
                "signature": "Set<R> convertSetByFlatMap(Collection<T> from,\n                                                       Function<? super T, ? extends U> mapper,\n                                                       Function<U, ? extends Stream<? extends R>> func)",
                "full_signature": "public static Set<R> convertSetByFlatMap(Collection<T> from,\n                                                       Function<? super T, ? extends U> mapper,\n                                                       Function<U, ? extends Stream<? extends R>> func)",
                "class_method_signature": "CollectionUtils.convertSetByFlatMap(Collection<T> from,\n                                                       Function<? super T, ? extends U> mapper,\n                                                       Function<U, ? extends Stream<? extends R>> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc)",
                "modifiers": "public static",
                "return": "Map<K, T>",
                "signature": "Map<K, T> convertMap(Collection<T> from, Function<T, K> keyFunc)",
                "full_signature": "public static Map<K, T> convertMap(Collection<T> from, Function<T, K> keyFunc)",
                "class_method_signature": "CollectionUtils.convertMap(Collection<T> from, Function<T, K> keyFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc, Supplier<? extends Map<K, T>> supplier)",
                "modifiers": "public static",
                "return": "Map<K, T>",
                "signature": "Map<K, T> convertMap(Collection<T> from, Function<T, K> keyFunc, Supplier<? extends Map<K, T>> supplier)",
                "full_signature": "public static Map<K, T> convertMap(Collection<T> from, Function<T, K> keyFunc, Supplier<? extends Map<K, T>> supplier)",
                "class_method_signature": "CollectionUtils.convertMap(Collection<T> from, Function<T, K> keyFunc, Supplier<? extends Map<K, T>> supplier)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "modifiers": "public static",
                "return": "Map<K, V>",
                "signature": "Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "full_signature": "public static Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "class_method_signature": "CollectionUtils.convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction)",
                "modifiers": "public static",
                "return": "Map<K, V>",
                "signature": "Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction)",
                "full_signature": "public static Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction)",
                "class_method_signature": "CollectionUtils.convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, Supplier<? extends Map<K, V>> supplier)",
                "modifiers": "public static",
                "return": "Map<K, V>",
                "signature": "Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, Supplier<? extends Map<K, V>> supplier)",
                "full_signature": "public static Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, Supplier<? extends Map<K, V>> supplier)",
                "class_method_signature": "CollectionUtils.convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, Supplier<? extends Map<K, V>> supplier)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction, Supplier<? extends Map<K, V>> supplier)",
                "modifiers": "public static",
                "return": "Map<K, V>",
                "signature": "Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction, Supplier<? extends Map<K, V>> supplier)",
                "full_signature": "public static Map<K, V> convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction, Supplier<? extends Map<K, V>> supplier)",
                "class_method_signature": "CollectionUtils.convertMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc, BinaryOperator<V> mergeFunction, Supplier<? extends Map<K, V>> supplier)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMultiMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc)",
                "modifiers": "public static",
                "return": "Map<K, List<T>>",
                "signature": "Map<K, List<T>> convertMultiMap(Collection<T> from, Function<T, K> keyFunc)",
                "full_signature": "public static Map<K, List<T>> convertMultiMap(Collection<T> from, Function<T, K> keyFunc)",
                "class_method_signature": "CollectionUtils.convertMultiMap(Collection<T> from, Function<T, K> keyFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMultiMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "modifiers": "public static",
                "return": "Map<K, List<V>>",
                "signature": "Map<K, List<V>> convertMultiMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "full_signature": "public static Map<K, List<V>> convertMultiMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "class_method_signature": "CollectionUtils.convertMultiMap(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertMultiMap2",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "modifiers": "public static",
                "return": "Map<K, Set<V>>",
                "signature": "Map<K, Set<V>> convertMultiMap2(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "full_signature": "public static Map<K, Set<V>> convertMultiMap2(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "class_method_signature": "CollectionUtils.convertMultiMap2(Collection<T> from, Function<T, K> keyFunc, Function<T, V> valueFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "convertImmutableMap",
                "parameters": "(Collection<T> from, Function<T, K> keyFunc)",
                "modifiers": "public static",
                "return": "Map<K, T>",
                "signature": "Map<K, T> convertImmutableMap(Collection<T> from, Function<T, K> keyFunc)",
                "full_signature": "public static Map<K, T> convertImmutableMap(Collection<T> from, Function<T, K> keyFunc)",
                "class_method_signature": "CollectionUtils.convertImmutableMap(Collection<T> from, Function<T, K> keyFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "diffList",
                "parameters": "(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
                "modifiers": "public static",
                "return": "List<List<T>>",
                "signature": "List<List<T>> diffList(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
                "full_signature": "public static List<List<T>> diffList(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
                "class_method_signature": "CollectionUtils.diffList(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "containsAny",
                "parameters": "(Collection<?> source, Collection<?> candidates)",
                "modifiers": "public static",
                "return": "boolean",
                "signature": "boolean containsAny(Collection<?> source, Collection<?> candidates)",
                "full_signature": "public static boolean containsAny(Collection<?> source, Collection<?> candidates)",
                "class_method_signature": "CollectionUtils.containsAny(Collection<?> source, Collection<?> candidates)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "getFirst",
                "parameters": "(List<T> from)",
                "modifiers": "public static",
                "return": "T",
                "signature": "T getFirst(List<T> from)",
                "full_signature": "public static T getFirst(List<T> from)",
                "class_method_signature": "CollectionUtils.getFirst(List<T> from)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "findFirst",
                "parameters": "(Collection<T> from, Predicate<T> predicate)",
                "modifiers": "public static",
                "return": "T",
                "signature": "T findFirst(Collection<T> from, Predicate<T> predicate)",
                "full_signature": "public static T findFirst(Collection<T> from, Predicate<T> predicate)",
                "class_method_signature": "CollectionUtils.findFirst(Collection<T> from, Predicate<T> predicate)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "findFirst",
                "parameters": "(Collection<T> from, Predicate<T> predicate, Function<T, U> func)",
                "modifiers": "public static",
                "return": "U",
                "signature": "U findFirst(Collection<T> from, Predicate<T> predicate, Function<T, U> func)",
                "full_signature": "public static U findFirst(Collection<T> from, Predicate<T> predicate, Function<T, U> func)",
                "class_method_signature": "CollectionUtils.findFirst(Collection<T> from, Predicate<T> predicate, Function<T, U> func)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "getMaxValue",
                "parameters": "(Collection<T> from, Function<T, V> valueFunc)",
                "modifiers": "public static",
                "return": "V",
                "signature": "V getMaxValue(Collection<T> from, Function<T, V> valueFunc)",
                "full_signature": "public static V getMaxValue(Collection<T> from, Function<T, V> valueFunc)",
                "class_method_signature": "CollectionUtils.getMaxValue(Collection<T> from, Function<T, V> valueFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "getMinValue",
                "parameters": "(List<T> from, Function<T, V> valueFunc)",
                "modifiers": "public static",
                "return": "V",
                "signature": "V getMinValue(List<T> from, Function<T, V> valueFunc)",
                "full_signature": "public static V getMinValue(List<T> from, Function<T, V> valueFunc)",
                "class_method_signature": "CollectionUtils.getMinValue(List<T> from, Function<T, V> valueFunc)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "getSumValue",
                "parameters": "(List<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator)",
                "modifiers": "public static",
                "return": "V",
                "signature": "V getSumValue(List<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator)",
                "full_signature": "public static V getSumValue(List<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator)",
                "class_method_signature": "CollectionUtils.getSumValue(List<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "getSumValue",
                "parameters": "(Collection<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator, V defaultValue)",
                "modifiers": "public static",
                "return": "V",
                "signature": "V getSumValue(Collection<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator, V defaultValue)",
                "full_signature": "public static V getSumValue(Collection<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator, V defaultValue)",
                "class_method_signature": "CollectionUtils.getSumValue(Collection<T> from, Function<T, V> valueFunc,\n                                                                     BinaryOperator<V> accumulator, V defaultValue)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "addIfNotNull",
                "parameters": "(Collection<T> coll, T item)",
                "modifiers": "public static",
                "return": "void",
                "signature": "void addIfNotNull(Collection<T> coll, T item)",
                "full_signature": "public static void addIfNotNull(Collection<T> coll, T item)",
                "class_method_signature": "CollectionUtils.addIfNotNull(Collection<T> coll, T item)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "singleton",
                "parameters": "(T obj)",
                "modifiers": "public static",
                "return": "Collection<T>",
                "signature": "Collection<T> singleton(T obj)",
                "full_signature": "public static Collection<T> singleton(T obj)",
                "class_method_signature": "CollectionUtils.singleton(T obj)",
                "testcase": false,
                "constructor": false
            },
            {
                "identifier": "newArrayList",
                "parameters": "(List<List<T>> list)",
                "modifiers": "public static",
                "return": "List<T>",
                "signature": "List<T> newArrayList(List<List<T>> list)",
                "full_signature": "public static List<T> newArrayList(List<List<T>> list)",
                "class_method_signature": "CollectionUtils.newArrayList(List<List<T>> list)",
                "testcase": false,
                "constructor": false
            }
        ],
        "file": "yudao-framework/yudao-common/src/main/java/cn/iocoder/yudao/framework/common/util/collection/CollectionUtils.java"
    },
    "focal_method": {
        "identifier": "diffList",
        "parameters": "(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
        "modifiers": "public static",
        "return": "List<List<T>>",
        "body": "public static <T> List<List<T>> diffList(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc) {\n        List<T> createList = new LinkedList<>(newList); // \u9ed8\u8ba4\u90fd\u8ba4\u4e3a\u662f\u65b0\u589e\u7684\uff0c\u540e\u7eed\u4f1a\u8fdb\u884c\u79fb\u9664\n        List<T> updateList = new ArrayList<>();\n        List<T> deleteList = new ArrayList<>();\n\n        // \u901a\u8fc7\u4ee5 oldList \u4e3a\u4e3b\u904d\u5386\uff0c\u627e\u51fa updateList \u548c deleteList\n        for (T oldObj : oldList) {\n            // 1. \u5bfb\u627e\u662f\u5426\u6709\u5339\u914d\u7684\n            T foundObj = null;\n            for (Iterator<T> iterator = createList.iterator(); iterator.hasNext(); ) {\n                T newObj = iterator.next();\n                // 1.1 \u4e0d\u5339\u914d\uff0c\u5219\u76f4\u63a5\u8df3\u8fc7\n                if (!sameFunc.apply(oldObj, newObj)) {\n                    continue;\n                }\n                // 1.2 \u5339\u914d\uff0c\u5219\u79fb\u9664\uff0c\u5e76\u7ed3\u675f\u5bfb\u627e\n                iterator.remove();\n                foundObj = newObj;\n                break;\n            }\n            // 2. \u5339\u914d\u6dfb\u52a0\u5230 updateList\uff1b\u4e0d\u5339\u914d\u5219\u6dfb\u52a0\u5230 deleteList \u4e2d\n            if (foundObj != null) {\n                updateList.add(foundObj);\n            } else {\n                deleteList.add(oldObj);\n            }\n        }\n        return asList(createList, updateList, deleteList);\n    }",
        "signature": "List<List<T>> diffList(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
        "full_signature": "public static List<List<T>> diffList(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
        "class_method_signature": "CollectionUtils.diffList(Collection<T> oldList, Collection<T> newList,\n                                             BiFunction<T, T, Boolean> sameFunc)",
        "testcase": false,
        "constructor": false,
        "invocations": [
            "iterator",
            "hasNext",
            "next",
            "apply",
            "remove",
            "add",
            "add",
            "asList"
        ]
    },
    "repository": {
        "url": "https://github.com/YunaiV/ruoyi-vue-pro",
        "repo_id": "332357698"
    }
}
```

Damn you love to scroll!