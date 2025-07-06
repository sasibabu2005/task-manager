function addTask() {
    const taskInput = document.getElementById("task-input");
    const taskText = taskInput.value.trim();
  
    if (taskText === "") return;
  
    const taskList = document.getElementById("task-list");
  
    const li = document.createElement("li");
    li.className = "task";
  
    li.innerHTML = `
      <span onclick="toggleTask(this)">${taskText}</span>
      <div class="actions">
        <button onclick="deleteTask(this)">Delete</button>
      </div>
    `;
  
    taskList.appendChild(li);
    taskInput.value = "";
  }
  
  function deleteTask(button) {
    const task = button.closest("li");
    task.remove();
  }
  
  function toggleTask(span) {
    span.parentElement.classList.toggle("completed");
  }
  