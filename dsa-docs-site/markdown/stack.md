# Stack Data Structure

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added to the stack is the first one to be removed. It behaves similarly to a stack of plates in a cafeteria.

## Structure and Visual Representation

In a Stack, all insertions and deletions are restricted to a single end called the **Top** of the stack.

```mermaid
graph TD
    subgraph Stack representation
        Top[Top of Stack] --> E[Element 4]
        E --> D[Element 3]
        D --> C[Element 2]
        C --> B[Element 1]
        style Top fill:#8b5cf6,stroke:#333,stroke-width:2px,color:#fff
        style E fill:#06b6d4,stroke:#333,stroke-width:1px,color:#fff
        style B fill:#1e293b,stroke:#333,stroke-width:1px,color:#fff
    end
```

## Standard Stack Operations

| Operation | Description | Time Complexity | Space Complexity |
| :--- | :--- | :---: | :---: |
| **Push** | Adds an element to the top of the stack | $O(1)$ | $O(1)$ |
| **Pop** | Removes and returns the top element of the stack | $O(1)$ | $O(1)$ |
| **Peek / Top** | Returns the top element without removing it | $O(1)$ | $O(1)$ |
| **isEmpty** | Checks if the stack is empty | $O(1)$ | $O(1)$ |
| **isFull** | Checks if the stack is full (for array-based implementations) | $O(1)$ | $O(1)$ |

---

## Step-by-Step Operation Diagrams

### 1. Push Operation
Adding `Element 5` to the stack. The top pointer moves up.

```mermaid
graph LR
    subgraph Before Push
        direction TB
        t1[Top] --> d4[Element 4]
        d4 --> d3[Element 3]
    end
    subgraph After Push
        direction TB
        t2[Top] --> d5[New Element 5]
        d5 --> d4b[Element 4]
        d4b --> d3b[Element 3]
        style d5 fill:#8b5cf6,color:#fff
    end
```

### 2. Pop Operation
Removing the top element (`Element 4`). The top pointer shifts down to the next element.

```mermaid
graph LR
    subgraph Before Pop
        direction TB
        t1[Top] --> d4[Element 4]
        d4 --> d3[Element 3]
        style d4 fill:#f43f5e,color:#fff
    end
    subgraph After Pop
        direction TB
        t2[Top] --> d3b[Element 3]
        style d3b fill:#8b5cf6,color:#fff
    end
```

---

## Java Implementation Examples

### Array-Based Stack
```java
public class ArrayStack {
    private int[] arr;
    private int top;
    private int capacity;

    public ArrayStack(int size) {
        arr = new int[size];
        capacity = size;
        top = -1;
    }

    public void push(int val) {
        if (top == capacity - 1) {
            throw new StackOverflowError("Stack is Full");
        }
        arr[++top] = val;
    }

    public int pop() {
        if (top == -1) {
            throw new RuntimeException("Stack is Empty");
        }
        return arr[top--];
    }

    public int peek() {
        if (top == -1) {
            throw new RuntimeException("Stack is Empty");
        }
        return arr[top];
    }
}
```
