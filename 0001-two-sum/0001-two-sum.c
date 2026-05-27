/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

#define TABLE_SIZE 23

typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

Node* hashTable[TABLE_SIZE];

int hash(int key) {
    if (key < 0)
        key = -1*key;

    return key % TABLE_SIZE;
}

void insert(int key, int value) {

    int index = hash(key);

    Node* newNode = (Node*)malloc(sizeof(Node));

    newNode->key = key;
    newNode->value = value;

    newNode->next = hashTable[index];

    hashTable[index] = newNode;
}

int search(int key) {

    int index = hash(key);

    Node* temp = hashTable[index];

    while (temp != NULL) {

        if (temp->key == key) {
            return temp->value;
        }

        temp = temp->next;
    }

    return -1;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    // initialize hash table with NULL
    for (int i = 0; i < TABLE_SIZE; i++) {
        hashTable[i] = NULL;
    }

    int *result = (int*)malloc(2 * sizeof(int));

    for (int i = 0; i < numsSize; i++) {

        int difference = target - nums[i];

        int foundIndex = search(difference);

        if (foundIndex != -1) {

            result[0] = foundIndex;
            result[1] = i;

            *returnSize = 2;

            return result;
        }

        insert(nums[i], i);
    }

    *returnSize = 0;

    return NULL;
}
