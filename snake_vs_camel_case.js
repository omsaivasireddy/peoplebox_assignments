function snakeToCamelCase(obj) {
    const result= {};
    for (const key in obj) {
        const camelKey = key.replace(/_([a-z])/g, (match, letter) => letter.toUpperCase());
        result[camelKey] = obj[key];
    }
    return result;
}

const snakeObj = {
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john.doe@example.com"
};

const camelObj = snakeToCamelCase(snakeObj);
console.log(camelObj);

// Python code to convert snake_case to camelCase

// def snake_to_camel_case(obj):
//     result = {}
//     for key in obj:
//         # Split the key by underscore and capitalize each word except the first one
//         words = key.split('_')
//         camel_key = words[0] + ''.join(word.capitalize() for word in words[1:])
//         result[camel_key] = obj[key]
//     return result

// snake_obj = {
//     "first_name": "John",
//     "last_name": "Doe",
//     "email_address": "john.doe@example.com"
// }

// camel_obj = snake_to_camel_case(snake_obj)
// print(camel_obj)