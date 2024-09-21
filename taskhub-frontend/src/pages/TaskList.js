// src/pages/TaskList.js
import React from 'react';
import { useSelector } from 'react-redux';
import TaskItem from '../components/TaskItem';

const TaskList = () => {
  const tasks = useSelector(state => state.tasks.tasks);

  return (
    <div>
      {tasks.map(task => (
        <TaskItem key={task.id} task={task} />
      ))}
    </div>
  );
};

export default TaskList;