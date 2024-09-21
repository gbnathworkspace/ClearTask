// src/components/TaskItem.js
import React from 'react';

const TaskItem = ({ task }) => {
    return (
        <div>
            <h2>{task.title}</h2>
            <p>{task.description}</p>
        </div>
    );
};

export default TaskItem;