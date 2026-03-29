# Project Title
AI-Based Interview Question Generator

# Abstract
The AI-Based Interview Question Generator is a web application designed to help students and job seekers prepare for technical interviews. Built using Python and Flask, the system employs a rule-based AI knowledge base to generate relevant interview questions tailored to a user's selected domain, difficulty level, and question type. The application features a user-friendly interface that dynamically presents questions across various topics such as Java, Python, DSA, Web Development, and DBMS, making it an excellent educational tool and a suitable college mini-project demonstrating basic Artificial Intelligence techniques.

# Introduction
Interview preparation can be overwhelming given the vast amount of technical subjects ranging from basic programming to complex system design. The AI-Based Interview Question Generator addresses this challenge by providing a structured, targeted practice environment. By leveraging a rule-based inference system, the project filters a comprehensive knowledge base to deliver highly specific questions. This project demonstrates how simple AI concepts like knowledge representation and rule-based logic can be implemented within a modern web framework to solve a practical problem.

# Problem Statement
Students and professionals often struggle to find categorized, level-appropriate interview questions for specific technical subjects. Generic question banks are frequently disorganized, making it difficult to practice effectively for a particular role or skill level. There is a need for an automated system that intelligently selects and presents questions based on user-defined criteria.

# Objectives
1. To develop a user-friendly web interface for selecting technical domains and difficulty levels.
2. To build an AI knowledge-based system using rule-based logic to evaluate user inputs.
3. To provide an extensive repository of categorized questions spanning subjects like DSA, OS, DBMS, and various programming languages.
4. To dynamically generate and beautifully present relevant interview questions to the user.

# Feasibility Study
**Technical Feasibility:** The project utilizes Python, Flask, HTML, and CSS, which are well-documented, freely available, and lightweight technologies, making it highly feasible to develop and deploy.
**Operational Feasibility:** The clean and intuitive UI ensures users of all technical backgrounds can operate the system without prior training.
**Economic Feasibility:** The project relies entirely on open-source technologies, resulting in zero software cost, making it perfect for an academic mini-project.

# AI Technique Used
**Knowledge-Based System (KBS):** The application relies on a knowledge-based approach, which is a form of Artificial Intelligence that attempts to capture human expertise to support decision-making. Specifically, the system uses an *inference engine* (the Python filtering logic) to query a *knowledge base* (the structured dataset of questions) to arrive at a conclusion (the generated list of questions).

# Knowledge Representation using Rules
The knowledge in this system is structured as factual records (dictionaries) possessing attributes (Domain, Level, Type). The intelligence is represented using **Production Rules** (IF-THEN statements).
For example:
*IF* `Domain == "Python"` *AND* `Level == "Beginner"` *AND* `Type == "Coding"` *THEN* generate Python beginner coding questions.

# System Architecture
1. **Presentation Layer (Frontend):** HTML and CSS forms where the user inputs their preferences (Domain, Level, Type).
2. **Application Layer (Backend Server):** Flask framework handling incoming HTTP requests and routing.
3. **Inference Engine (AI Logic):** Python logic applying IF-THEN rules to match the user's constraints against the knowledge base.
4. **Knowledge Base (Data):** A structured Python list containing all specific interview questions with their metadata tags.

# Workflow of the System
1. User opens the application in a web browser.
2. User selects the desired Subject, Difficulty, and Question Type from the dropdown menus.
3. User submits the request.
4. The Flask backend receives the form data.
5. The Rule-Based AI engine parses the inputs and iterated through the Knowledge Base.
6. The engine checks IF-THEN conditions; if all rules match, the question is added to the result pool.
7. The backend renders the resulting questions dynamically into the results HTML page.
8. The browser displays the filtered questions to the user.

# Algorithm
1. Start.
2. Initialize the `knowledge_base` (List of dictionaries containing questions).
3. Wait for HTTP POST request on `/generate`.
4. Extract `domain`, `level`, and `type` from the request payload.
5. Initialize an empty list `results`.
6. For each `question` in `knowledge_base`:
   a. Keep boolean `rule_match = True`.
   b. IF `domain` is specified AND `question.domain` != `domain`, SET `rule_match = False`.
   c. IF `level` is specified AND `question.level` != `level`, SET `rule_match = False`.
   d. IF `type` is specified AND `question.type` != `type`, SET `rule_match = False`.
   e. IF `rule_match` is True, APPEND `question` to `results`.
7. Return `results` to the `result.html` template.
8. Stop.

# Sample Rules
```python
# Rule 1
IF (input_domain != "Any") THEN check if question["domain"] == input_domain
# Rule 2
IF (input_level != "Any") THEN check if question["level"] == input_level
# Rule 3
IF (input_type != "Any") THEN check if question["type"] == input_type
```

# Sample Dataset
```json
{
    "domain": "DSA", 
    "level": "Intermediate", 
    "type": "Theory", 
    "question": "Explain the working principles of QuickSort and MergeSort."
}
```

# Sample Input and Output
**Input:** 
- Domain: Python
- Level: Beginner
- Type: Coding

**Output:**
- "Write a Python script to check if a number is prime."

# Advantages
1. **Highly Customizable:** Users can create highly targeted queries (e.g., only Advanced Java Scenario questions).
2. **Easy to Expand:** Adding new questions simply involves adding new dictionaries to the knowledge base without altering the logic.
3. **Fast Execution:** Rule-based evaluation runs purely in memory, resulting in near-instantaneous responses.
4. **No Database Configuration Required:** Ideal for student deployment.

# Limitations
1. **Static Knowledge Base:** The questions are hardcoded and cannot be updated dynamically by a user without changing the source code.
2. **Exact Matching:** The rule engine relies on exact keyword matching, limiting its ability to understand fuzzy or natural language queries.
3. **No Learning Loop:** As a pure rule-based system, it does not use machine learning to adapt or learn from user behavior over time.

# Future Scope
1. **Integration of Database:** Connect the application to a SQL/NoSQL database for persistent, dynamic storage of questions.
2. **Natural Language Processing (NLP):** Allow users to type their request ("I want hard Java coding questions") instead of using dropdowns.
3. **User Authentication & Progress Tracking:** Allow users to log in, save their generated tests, and track their performance over time.
4. **Machine Learning Inference:** Implement a Recommendation System that analyzes a user's mock test scores to automatically suggest the next set of questions.

# Conclusion
The AI-Based Interview Question Generator successfully demonstrates the practical implementation of a rule-based AI system within a modern web context. By isolating technical knowledge into a structured format and utilizing production rules, the application quickly and accurately retrieves highly relevant interview material. The resulting Flask application is lightweight, responsive, and serves as an excellent foundational mini-project highlighting the core principles of Knowledge-Based Systems in Artificial Intelligence.

---

# Industry Problem Context & Mapping
*(Note: The following context relates to optimal path optimization and route finding algorithms in Artificial Intelligence, such as A* and Best First Search. Added as requested for Artificial Intelligence (N-PCCCS601T) - Department of Computer Science and Engineering, S.B.J.I.T.M.R., Nagpur)*

## 1. Industry Problem Context
In the IT industry, the problem of finding an optimal route between locations appears in:
- Navigation and map services (Google Maps–like systems)
- Logistics and delivery platforms
- Cloud network routing
- Data center traffic optimization
- Ride-sharing applications

The core objective is to minimize cost, such as distance, time, bandwidth, or latency.

## 2. Feasibility in IT Systems
- Real-world locations, servers, or nodes are modeled as graphs.
- Nodes represent locations/routers/servers.
- Edges represent roads, links, or network connections.
- Edge weights represent distance, time, congestion, or cost.
- Large-scale graphs are stored using graph databases or in-memory structures.

Hence, graph-based simulation is highly feasible and scalable in industry.

## 3. AI Techniques Used in Industry
- **A* Search**
  - Used for fast and optimal path finding
  - Combines actual cost + heuristic estimate
- **Best First Search**
  - Used when speed is prioritized over optimality
- **Heuristics Used**
  - Straight-line distance (maps)
  - Estimated latency (networks)
  - Historical traffic patterns (advanced systems)

These techniques ensure real-time performance.

## 4. Representation/Modeling in Industry Systems
- **State Space Graph**
  - Each state = current location/node
  - Transitions = possible next locations
- **Graphs are:**
  - Dynamically updated (traffic, failures)
  - Distributed across systems
  - Often implemented using adjacency lists or graph engines.

## 5. Tools & Technologies in Industry
- Python / Java / C++ for algorithm implementation
- Graph frameworks (e.g., internal graph engines, NetworkX for prototyping)
- Cloud services for large-scale computation
- APIs to fetch real-time data (traffic, network load)

Python + NetworkX is commonly used for prototyping and proof-of-concept, before deployment in production systems.

## 6. Industry-Level Outcome
- Optimal route computation in milliseconds
- Comparison of multiple routing strategies
- Reduced cost and improved efficiency
- Performance metrics such as:
  - Path cost
  - Execution time
  - Number of nodes expanded

## 7. Real-World Industry Example/use
- **Navigation Apps:** Find fastest route avoiding traffic
- **Logistics Companies:** Optimize delivery routes
- **Cloud Providers:** Route data packets efficiently
- **IT Service Providers:** Optimize workflow or data pipeline paths (this point can be included in the project)
