# 📝 To-Do List Chatbot (Tkinter GUI)

## 📌 Problem Statement
Managing daily tasks can often become overwhelming without a simple and interactive tool.  
The goal of this project is to design a **chatbot-style To-Do List application** with a graphical interface that allows users to:
- Add tasks
- View pending/completed tasks
- Mark tasks as done  
All while keeping the interface intuitive and beginner-friendly.

---

## 🛠️ Approach Used
- **Chatbot-inspired design**: Instead of a plain list manager, the application responds with messages like a chatbot.
- **GUI with Tkinter**: Provides buttons, text areas, and message boxes for user interaction.
- **Task management logic**: Each task is stored with a status flag (`done` or `not done`).
- **Incremental development**: Started with core task operations, then integrated GUI components.

---

## ⚙️ Logic and Implementation
1. **Task Storage**  
   - Tasks are stored in a Python list as dictionaries:  
     ```python
     {"task": "Buy groceries", "done": False}
     ```

2. **Core Functionalities**  
   - `add_task(task)`: Adds a new task with default status ❌.  
   - `show_tasks()`: Displays all tasks with status indicators (✅ or ❌).  
   - `mark_done(index)`: Marks a task as completed based on its index.

3. **GUI Components**  
   - **Entry Box**: For entering new tasks.  
   - **Buttons**:  
     - Add Task  
     - Show Tasks  
     - Mark Done  
   - **Text Area**: Displays the task list.  
   - **Message Boxes**: Provide feedback (info, warning, error).

4. **Flow**  
   - User enters a task → clicks **Add Task** → task stored.  
   - User clicks **Show Tasks** → tasks displayed with status.  
   - User enters task number → clicks **Mark Done** → task updated.

---

## 💡 Innovations
- **Chatbot-style feedback**: Instead of silent updates, the app responds with messages like *“Added: 'Buy groceries'”* or *“Marked 'Homework' as done ✅”*.
- **Emoji-based status indicators**: ✅ for completed tasks, ❌ for pending tasks — making the interface more engaging.
- **Error handling**: Invalid inputs (empty task or wrong index) trigger warnings/errors via message boxes.

---

## 🚧 Challenges Faced
- **Index handling**: Mapping user-friendly task numbers (1-based) to Python list indices (0-based).
- **GUI synchronization**: Ensuring the text area updates correctly after each operation.
- **Input validation**: Preventing crashes when users enter invalid task numbers or leave fields empty.
- **Balancing simplicity vs. features**: Keeping the app lightweight while adding chatbot-like interactivity.

---

## ✅ Conclusion
This project demonstrates how **Python + Tkinter** can be used to build a simple yet interactive To-Do List Chatbot.  
It combines **task management logic** with a **user-friendly GUI**, making everyday task tracking more engaging.  
Future improvements could include:
- Persistent storage (saving tasks to a file or database).
- Task deletion and editing features.
- Enhanced UI with themes and layouts.

---

👨‍💻 Developed by
[SHARATH S] 
[SIDDARAM MAINDARGI] 
[VENU MADHAV K T]  
