function snakeToCamelCase(obj) {
    const result= {};
    for (const key in obj) {
        const camelKey = key.replace(/_([a-z])/g, (match, letter) => letter.toUpperCase());
        result[camelKey] = obj[key];
    }
    return result;
}

// Example usage:
const snakeObj = {
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john.doe@example.com"
};

const camelObj = snakeToCamelCase(snakeObj);