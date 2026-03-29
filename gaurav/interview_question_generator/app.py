from flask import Flask, render_template, request

app = Flask(__name__)

# Sample dataset of interview questions
# Contains over 50 questions categorized by domain, level, and type.
knowledge_base = [
    # Java Questions
    {"domain": "Java", "level": "Beginner", "type": "Theory", "question": "What are the core concepts of OOPs in Java?"},
    {"domain": "Java", "level": "Beginner", "type": "Coding", "question": "Write a Java program to print 'Hello World'."},
    {"domain": "Java", "level": "Intermediate", "type": "Theory", "question": "Explain the difference between final, finally, and finalize in Java."},
    {"domain": "Java", "level": "Intermediate", "type": "Scenario", "question": "How do you handle memory leaks in a Java application?"},
    {"domain": "Java", "level": "Advanced", "type": "Coding", "question": "Implement a thread-safe Singleton class in Java."},
    
    # Python Questions
    {"domain": "Python", "level": "Beginner", "type": "Theory", "question": "What are the main differences between Python 2 and Python 3?"},
    {"domain": "Python", "level": "Beginner", "type": "Coding", "question": "Write a Python script to check if a number is prime."},
    {"domain": "Python", "level": "Intermediate", "type": "Theory", "question": "Explain generators and iterators in Python."},
    {"domain": "Python", "level": "Intermediate", "type": "Scenario", "question": "How would you optimize a Python script processing a large dataset?"},
    {"domain": "Python", "level": "Advanced", "type": "Coding", "question": "Write a Python decorator that measures execution time of a function."},
    {"domain": "Python", "level": "Advanced", "type": "Theory", "question": "Deep explanation of Global Interpreter Lock (GIL)."},

    # DSA Questions
    {"domain": "DSA", "level": "Beginner", "type": "Theory", "question": "What is the difference between Array and Linked List?"},
    {"domain": "DSA", "level": "Beginner", "type": "Coding", "question": "Write a function to reverse a string in-place."},
    {"domain": "DSA", "level": "Intermediate", "type": "Theory", "question": "Explain the working principles of QuickSort and MergeSort."},
    {"domain": "DSA", "level": "Intermediate", "type": "Coding", "question": "Implement a binary search tree (BST) and its traversal methods."},
    {"domain": "DSA", "level": "Advanced", "type": "Coding", "question": "Solve the N-Queens problem using backtracking."},
    {"domain": "DSA", "level": "Advanced", "type": "Scenario", "question": "Design a data structure for an LRU Cache."},

    # C Questions
    {"domain": "C", "level": "Beginner", "type": "Theory", "question": "What are pointers in C?"},
    {"domain": "C", "level": "Beginner", "type": "Coding", "question": "Write a C program to swap two numbers without using a third variable."},
    {"domain": "C", "level": "Intermediate", "type": "Theory", "question": "Explain malloc, calloc, realloc, and free."},
    {"domain": "C", "level": "Advanced", "type": "Coding", "question": "Implement a doubly linked list in C."},
    
    # C++ Questions
    {"domain": "C++", "level": "Beginner", "type": "Theory", "question": "Explain virtual functions in C++."},
    {"domain": "C++", "level": "Intermediate", "type": "Theory", "question": "What is the difference between function overloading and overriding?"},
    {"domain": "C++", "level": "Advanced", "type": "Scenario", "question": "How does C++ handle exception safety in constructors?"},

    # Web Development
    {"domain": "Web Development", "level": "Beginner", "type": "Theory", "question": "What is the difference between HTML, CSS, and JS?"},
    {"domain": "Web Development", "level": "Intermediate", "type": "Scenario", "question": "How do you improve performance and load time of a webpage?"},
    {"domain": "Web Development", "level": "Advanced", "type": "Coding", "question": "Create a responsive navigation bar using Flexbox."},
    
    # DBMS
    {"domain": "DBMS", "level": "Beginner", "type": "Theory", "question": "What is normalization? Explain 1NF, 2NF, 3NF."},
    {"domain": "DBMS", "level": "Beginner", "type": "Coding", "question": "Write a SQL query to find the second highest salary."},
    {"domain": "DBMS", "level": "Intermediate", "type": "Scenario", "question": "How do you handle concurrent transactions in a database?"},
    {"domain": "DBMS", "level": "Advanced", "type": "Theory", "question": "Explain ACID properties in detail with examples."},

    # OS
    {"domain": "OS", "level": "Beginner", "type": "Theory", "question": "What is a deadlock and what are its necessary conditions?"},
    {"domain": "OS", "level": "Intermediate", "type": "Theory", "question": "Explain different memory management techniques (paging, segmentation)."},
    {"domain": "OS", "level": "Advanced", "type": "Scenario", "question": "How do you troubleshoot a system that is constantly out of memory?"},

    # Computer Networks (CN)
    {"domain": "CN", "level": "Beginner", "type": "Theory", "question": "What is the OSI model? Name its layers."},
    {"domain": "CN", "level": "Intermediate", "type": "Theory", "question": "Explain the difference between TCP and UDP."},
    {"domain": "CN", "level": "Advanced", "type": "Scenario", "question": "How would you trace and resolve high network latency in a distributed app?"},

    # Aptitude
    {"domain": "Aptitude", "level": "Beginner", "type": "Theory", "question": "A train running at 60 kmph crosses a pole in 9s. What is the length of the train?"},
    {"domain": "Aptitude", "level": "Intermediate", "type": "Scenario", "question": "A can do a work in 10 days, B in 15 days. How long if they work together?"},
    {"domain": "Aptitude", "level": "Advanced", "type": "Coding", "question": "Solve a complex logical reasoning sequence puzzle (provide the logic)."}
]

# Adding more questions to easily exceed the 50 threshold
extra_questions = [
    # Java expanded
    {"domain": "Java", "level": "Beginner", "type": "Theory", "question": "What is the JDK, JRE, and JVM?"},
    {"domain": "Java", "level": "Beginner", "type": "Theory", "question": "Explain public static void main(String args[])."},
    {"domain": "Java", "level": "Beginner", "type": "Coding", "question": "Write a Java program to check if a number is even or odd."},
    {"domain": "Java", "level": "Intermediate", "type": "Coding", "question": "Write a Java program to reverse a string."},
    {"domain": "Java", "level": "Intermediate", "type": "Theory", "question": "Explain method overloading vs method overriding."},
    {"domain": "Java", "level": "Intermediate", "type": "Scenario", "question": "If you get a NullPointerException, how do you trace it?"},
    {"domain": "Java", "level": "Advanced", "type": "Theory", "question": "Explain the internal working of HashMap in Java."},
    {"domain": "Java", "level": "Advanced", "type": "Scenario", "question": "Explain how you would tune the JVM Garbage Collector for a low-latency application."},
    
    # Python expanded
    {"domain": "Python", "level": "Beginner", "type": "Theory", "question": "What are lists and tuples? How are they different?"},
    {"domain": "Python", "level": "Beginner", "type": "Coding", "question": "Write a Python script to find the factorial of a number."},
    {"domain": "Python", "level": "Beginner", "type": "Scenario", "question": "How would you read a large 10GB text file in Python?"},
    {"domain": "Python", "level": "Intermediate", "type": "Coding", "question": "Write a list comprehension to square numbers in a list."},
    {"domain": "Python", "level": "Intermediate", "type": "Theory", "question": "Explain the use of `*args` and `**kwargs` in Python functions."},
    {"domain": "Python", "level": "Intermediate", "type": "Scenario", "question": "How do you handle circular imports in large Python projects?"},
    {"domain": "Python", "level": "Advanced", "type": "Theory", "question": "Explain metaprogramming and metaclasses in Python."},
    {"domain": "Python", "level": "Advanced", "type": "Scenario", "question": "You are migrating a Python 2 script to Python 3. What are the key areas to watch?"},

    # DSA expanded
    {"domain": "DSA", "level": "Beginner", "type": "Theory", "question": "Explain Stack vs Queue."},
    {"domain": "DSA", "level": "Beginner", "type": "Coding", "question": "Write a function to check if a string is a palindrome."},
    {"domain": "DSA", "level": "Beginner", "type": "Scenario", "question": "When would you choose a linked list over an array?"},
    {"domain": "DSA", "level": "Intermediate", "type": "Coding", "question": "Write a program to detect a loop in a linked list."},
    {"domain": "DSA", "level": "Intermediate", "type": "Scenario", "question": "If an algorithm is O(N^2) time, what data structures could reduce it?"},
    {"domain": "DSA", "level": "Advanced", "type": "Theory", "question": "Explain the working principles of a Red-Black tree."},
    {"domain": "DSA", "level": "Advanced", "type": "Scenario", "question": "Design an algorithm to find the shortest path in a weighted city map."},

    # C expanded
    {"domain": "C", "level": "Beginner", "type": "Theory", "question": "What is a macro in C?"},
    {"domain": "C", "level": "Beginner", "type": "Scenario", "question": "Why do we include <stdio.h> in C programs?"},
    {"domain": "C", "level": "Intermediate", "type": "Coding", "question": "Write a program to find the factorial of a number using recursion."},
    {"domain": "C", "level": "Intermediate", "type": "Scenario", "question": "How would you find a memory leak using Valgrind?"},
    {"domain": "C", "level": "Advanced", "type": "Theory", "question": "How is pointer arithmetic different from regular arithmetic?"},
    {"domain": "C", "level": "Advanced", "type": "Scenario", "question": "How do you debug a segmentation fault in C?"},

    # C++ expanded
    {"domain": "C++", "level": "Beginner", "type": "Theory", "question": "What is the difference between struct and class in C++?"},
    {"domain": "C++", "level": "Intermediate", "type": "Coding", "question": "Write a C++ program using unique_ptr."},
    {"domain": "C++", "level": "Intermediate", "type": "Scenario", "question": "When would you prefer passing by reference over value?"},
    {"domain": "C++", "level": "Advanced", "type": "Coding", "question": "Implement a binary search tree template class."},
    {"domain": "C++", "level": "Advanced", "type": "Theory", "question": "Explain move semantics and rvalue references."},

    # Web Dev expanded
    {"domain": "Web Development", "level": "Beginner", "type": "Coding", "question": "Write HTML for a simple login form."},
    {"domain": "Web Development", "level": "Beginner", "type": "Scenario", "question": "A user complains a website is broken on mobile. What CSS do you check?"},
    {"domain": "Web Development", "level": "Intermediate", "type": "Theory", "question": "Explain the Virtual DOM in React."},
    {"domain": "Web Development", "level": "Intermediate", "type": "Coding", "question": "Write a fetch API request handling promises and errors."},
    {"domain": "Web Development", "level": "Advanced", "type": "Theory", "question": "Explain Server-Side Rendering (SSR) vs Static Generation."},
    {"domain": "Web Development", "level": "Advanced", "type": "Scenario", "question": "How do you implement secure JWT authentication flows?"},

    # DBMS expanded
    {"domain": "DBMS", "level": "Beginner", "type": "Theory", "question": "What is a primary key and foreign key?"},
    {"domain": "DBMS", "level": "Beginner", "type": "Scenario", "question": "If your DB server runs out of disk space, how do you free it up safely?"},
    {"domain": "DBMS", "level": "Intermediate", "type": "Theory", "question": "Difference between clustered and non-clustered index?"},
    {"domain": "DBMS", "level": "Intermediate", "type": "Coding", "question": "Write a query to find all employees assigned to a specific department."},
    {"domain": "DBMS", "level": "Advanced", "type": "Theory", "question": "Explain database indexing and its trade-offs."},
    {"domain": "DBMS", "level": "Advanced", "type": "Scenario", "question": "A production query is deadlocking. How do you troubleshoot?"},

    # OS expanded
    {"domain": "OS", "level": "Beginner", "type": "Theory", "question": "What is the difference between a process and a thread?"},
    {"domain": "OS", "level": "Beginner", "type": "Scenario", "question": "A process has hung at 100% CPU. What steps do you take on Linux?"},
    {"domain": "OS", "level": "Intermediate", "type": "Theory", "question": "Explain CPU scheduling algorithms (Round Robin, SJF)."},
    {"domain": "OS", "level": "Intermediate", "type": "Coding", "question": "Write a bash command to find zombie processes."},
    {"domain": "OS", "level": "Advanced", "type": "Theory", "question": "Explain virtual memory and thrashing."},
    {"domain": "OS", "level": "Advanced", "type": "Scenario", "question": "Design a mutual exclusion lock handling algorithm."},

    # CN expanded
    {"domain": "CN", "level": "Beginner", "type": "Theory", "question": "What is an IP address and MAC address?"},
    {"domain": "CN", "level": "Beginner", "type": "Scenario", "question": "WiFi connects but 'No Internet'. How do you troubleshoot?"},
    {"domain": "CN", "level": "Intermediate", "type": "Theory", "question": "Explain how DNS works."},
    {"domain": "CN", "level": "Intermediate", "type": "Scenario", "question": "Ping works but SSH times out. What firewall issue is likely happening?"},
    {"domain": "CN", "level": "Advanced", "type": "Scenario", "question": "Explain the exact steps that occur when a user types a URL into a browser."},
    {"domain": "CN", "level": "Advanced", "type": "Coding", "question": "Write a basic socket server code that accepts incoming connections."},
    
    # Aptitude expanded
    {"domain": "Aptitude", "level": "Beginner", "type": "Scenario", "question": "Explain your logical approach estimating the number of gas stations in a country."},
    {"domain": "Aptitude", "level": "Intermediate", "type": "Theory", "question": "What is the mathematical concept of permutations vs combinations?"},
    {"domain": "Aptitude", "level": "Advanced", "type": "Scenario", "question": "You have 8 balls. One is slightly heavier. Use a balance scale twice to find it."}
]

knowledge_base.extend(extra_questions)

# Rule Engine Logic
def infer_questions(domain, level, type_val):
    results = []
    # IF-THEN rules for exact question matching based on Knowledge System
    for q in knowledge_base:
        rule_match = True
        
        # Rule 1: Check Domain Filtering
        if domain and domain != "Any":
            if q["domain"] != domain:
                rule_match = False
                
        # Rule 2: Check Difficulty Level Filtering
        if level and level != "Any":
            if q["level"] != level:
                rule_match = False
                
        # Rule 3: Check Question Type Filtering
        if type_val and type_val != "Any":
            if q["type"] != type_val:
                rule_match = False
                
        # Rule matches the exact criteria
        if rule_match:
            results.append(q)
            
    # AI Engine Fallback Rule: If strict filtering results in few questions, 
    # relax the constraints (level/type) to ensure more questions are shown for the selected domain.
    if len(results) < 5 and domain and domain != "Any":
        for q in knowledge_base:
            if q["domain"] == domain and q not in results:
                results.append(q)
            # Cap the fallback size so it doesn't overwhelm, but provides "more questions"
            if len(results) >= 8:
                break
                
    return results

@app.route("/", methods=["GET"])
def index():
    # Render the input form on GET request
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Extract user inputs from logical form
    domain = request.form.get("domain")
    level = request.form.get("level")
    type_val = request.form.get("type")
    
    # Applying the AI Rule-Based Logic
    matched_questions = infer_questions(domain, level, type_val)
    
    # Feedback variables to show user what filters triggered the results
    return render_template("result.html", 
                           questions=matched_questions, 
                           domain=domain, 
                           level=level, 
                           type_val=type_val)

if __name__ == "__main__":
    app.run(debug=True)
