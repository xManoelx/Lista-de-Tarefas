# ✅ Gerenciador de Lista de Tarefas - Python CLI

A complete command-line task manager built in Python, featuring full CRUD operations for managing daily tasks. This terminal-based application provides an intuitive menu system for adding, viewing, updating, completing, and removing tasks efficiently.

## 📸 Preview

```
Menu do Gerenciador de Lista de Tarefas
1. Adicionar tarefa
2. Ver tarefas
3. Atualizar tarefa
4. Completar tarefa
5. Remover tarefa
6. Sair

Lista de tarefas:
1. [✔] Estudar Python
2. [ ] Fazer exercícios
3. [ ] Revisar código
```

## 📋 About This Project

This project is a comprehensive task management system built entirely in Python, demonstrating core programming concepts through a practical, real-world application. The CLI interface provides all essential task management features while maintaining simplicity and ease of use.

### Core Functionality:
- **Add Tasks**: Create new tasks with descriptive names
- **View Tasks**: Display all tasks with completion status indicators
- **Update Tasks**: Modify existing task names
- **Complete Tasks**: Mark tasks as finished with visual checkmarks
- **Remove Tasks**: Delete all completed tasks at once
- **Interactive Menu**: User-friendly navigation system

## 🛠️ Technologies Used

- **Python 3** - Core programming language
  - Lists and dictionaries for data management
  - Control flow (loops, conditionals)
  - Functions and modular programming
  - String manipulation and formatting
  - User input handling and validation

## 🎯 Features

- ✅ **Complete CRUD Operations** - Create, Read, Update, Delete functionality
- ✅ **Interactive CLI Interface** - Menu-driven user experience
- ✅ **Task Status Tracking** - Visual indicators for completed tasks
- ✅ **Input Validation** - Error handling for invalid task indices
- ✅ **Batch Operations** - Remove all completed tasks at once
- ✅ **Persistent Session** - Tasks remain available during program execution
- ✅ **Clean Code Structure** - Modular functions for each operation

## 🔧 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/xManoelx/python-task-manager.git
   cd python-task-manager
   ```

2. **Run the application**
   ```bash
   python task_manager.py
   ```

3. **Follow the menu prompts**
   - Choose options 1-6 to perform different operations
   - Add tasks by typing their names
   - View tasks to see current status
   - Update, complete, or remove tasks as needed

## 💻 Code Structure

The application is organized into modular functions:

- **`addTask()`** - Adds new tasks to the list
- **`viewTask()`** - Displays all tasks with status indicators
- **`attTaskName()`** - Updates existing task names
- **`completeTask()`** - Marks tasks as completed
- **`deleteTask()`** - Removes all completed tasks
- **Main Loop** - Handles user interaction and menu navigation

## 📚 What I Learned

This project enhanced my Python programming skills in:

- **Data Structures**: Working with lists and dictionaries effectively
- **Function Design**: Creating reusable, modular code components
- **User Interface**: Building intuitive command-line interfaces
- **Input Validation**: Handling user errors and edge cases
- **Control Flow**: Implementing loops and conditional logic
- **String Formatting**: Creating readable output and status indicators
- **Problem Solving**: Breaking complex tasks into manageable functions

## 🌟 Technical Highlights

- **Modular Architecture**: Clean separation of concerns with dedicated functions
- **Error Handling**: Validation for task indices and user input
- **Data Management**: Efficient task storage using Python data structures
- **User Experience**: Intuitive menu system with clear feedback
- **Code Readability**: Well-structured code with descriptive variable names

## 🚀 Program Flow

1. **Main Menu**: Display available options
2. **User Selection**: Process user choice
3. **Function Execution**: Perform requested operation
4. **Feedback**: Show operation results
5. **Loop Continuation**: Return to menu until user exits

## 🔄 Future Improvements

- [ ] Add task persistence with file storage (JSON/CSV)
- [ ] Implement task priorities and categories
- [ ] Add due dates and deadline tracking
- [ ] Create task search and filtering functionality
- [ ] Add task statistics and progress tracking
- [ ] Implement data export capabilities
- [ ] Add colored terminal output for better UX

## 👨‍💻 Author

**Manoel Antonio**
- Junior Robot Programmer transitioning to Full Stack Development
- GitHub: [@xManoelx](https://github.com/xManoelx)
- Location: Caxias do Sul, RS, Brasil

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*From industrial robotics to Python programming - building practical solutions with clean, efficient code! 🤖🐍*
