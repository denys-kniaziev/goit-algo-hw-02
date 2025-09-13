# Woolf University. Basic Algorithms and Data Structures Course. Homework – Basic Data Structures

## Overview

This assignment introduces working with queues and deques to simulate request processing and check for palindromes.

---

## Task 1 – Request Queue Simulation

### Description

Develop a program that simulates the acceptance and processing of service requests:

* New requests are automatically generated with unique identifiers.
* Requests are added to a queue.
* Requests are then sequentially removed from the queue for "processing," simulating a service center.

### Requirements

* Use the `Queue` class from Python’s `queue` module.
* Implement a function **generate\_request()** that creates and enqueues a new request.
* Implement a function **process\_request()** that dequeues and processes a request if available; otherwise, indicate that the queue is empty.
* Main program loop should repeatedly generate and process requests until the user exits.

### Evaluation Criteria

* Correct use of `Queue` for request handling.
* Functions properly generate and process requests.
* Clear output indicating when requests are created, processed, or when the queue is empty.

---

## Task 2 – Palindrome Checker with Deque

### Description

Develop a function that checks if a given string is a palindrome:

* Add all characters of the string to a double-ended queue (`deque` from `collections`).
* Compare characters from both ends until the middle is reached.
* Ignore case and whitespace when checking.

### Requirements

* Function accepts a string as input.
* Converts string to a normalized form (lowercase, no spaces).
* Uses a deque to compare characters from front and back.
* Returns whether the string is a palindrome.

### Evaluation Criteria

* Proper use of `deque` for checking.
* Handles both even and odd length strings.
* Case-insensitive and whitespace-agnostic comparison.
* Clear and maintainable code.
