# 📁 Linked List
> A Python implementation of a singly linked list built from scratch, no built-in list, no shortcuts.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Data%20Structures-red?logo=python&logoColor=white)

## 📌 About

This project implements a singly linked list entirely from scratch using nested classes. Rather than relying on Python's built-in `list`, this builds the underlying structure manually, each node holds a value and a pointer to the next node, forming a chain. It was built to understand how data structures work at a lower level and to practice pointer-based thinking, nested classes, and traversal logic.

## 🧠 What I Learned

- **Nested classes** — Defining `Node` inside `LinkedList` to encapsulate the node structure within the class that uses it, rather than exposing it as a separate top-level class
- **Pointer-based thinking** — Each node holds a reference (`next`) to the next node rather than an index, which requires a fundamentally different mental model from Python lists
- **Traversal with a `while` loop** — Walking the chain from `self.head` by following `.next` pointers until reaching `None`, which marks the end of the list
- **Edge case handling in `remove()`** — Three distinct cases to handle: element not found, element is the head node, and element is somewhere in the middle — each requiring a different pointer update
- **Tracking state manually** — Maintaining `self.length` explicitly and incrementing/decrementing it on every add and remove, since there's no built-in `len()` for a custom structure
- **Why linked lists matter** — Understanding that while Python lists are more convenient, linked lists offer O(1) insertion at the head and are foundational to understanding how higher-level data structures like stacks, queues, and trees work

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |

## 💡 How It Works

Each `Node` stores an `element` and a `next` pointer. `LinkedList` maintains a reference to the first node (head) and tracks the total length.
```
head
 │
 ▼
[1] ──► [2] ──► [3] ──► None
```

| Method | Description |
|--------|-------------|
| `is_empty()` | Returns `True` if the list has no nodes |
| `add(element)` | Traverses to the last node and appends a new one |
| `remove(element)` | Traverses to find the element and relinks the surrounding nodes |

**Example Output:**
```
True    # is_empty() before adding
False   # is_empty() after adding 1 and 2
2       # length after adding 1 and 2
1       # length after removing 1
```

## 🚀 Future Improvements

- [ ] Add a `search(element)` method that returns the index of a value
- [ ] Add `insert(index, element)` to insert at a specific position
- [ ] Implement a `__str__` method to print the full chain visually (e.g. `1 → 2 → 3 → None`)
- [ ] Extend into a doubly linked list with both `next` and `previous` pointers
- [ ] Use the linked list as the foundation for a stack or queue implementation

## 📂 Project Structure
```
linked-list/
│
├── LinkedList.py    # Node and LinkedList classes with example usage
└── README.md
```

*Part of my Python learning journey 🐍 — diving into data structures and pointer based thinking*
