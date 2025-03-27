CREATE TABLE tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'pending',
        priority TEXT DEFAULT 'medium',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE tasks_history (
        history_id INTEGER PRIMARY KEY,
        task_id INTEGER,
        title TEXT,
        description TEXT,
        status TEXT,
        priority TEXT,
        operation TEXT NOT NULL,
        changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (task_id) REFERENCES tasks(id)
    );
CREATE TRIGGER tasks_insert_trigger
    AFTER INSERT ON tasks
    BEGIN
        INSERT INTO tasks_history (
            task_id, title, description, status, priority, 
            operation, changed_at
        )
        VALUES (
            NEW.id, NEW.title, NEW.description, NEW.status, 
            NEW.priority, 'INSERT', CURRENT_TIMESTAMP
        );
    END;
CREATE TRIGGER tasks_update_trigger
    AFTER UPDATE ON tasks
    BEGIN
        INSERT INTO tasks_history (
            task_id, title, description, status, priority, 
            operation, changed_at
        )
        VALUES (
            NEW.id, NEW.title, NEW.description, NEW.status, 
            NEW.priority, 'UPDATE', CURRENT_TIMESTAMP
        );
    END;
CREATE TRIGGER tasks_delete_trigger
    AFTER DELETE ON tasks
    BEGIN
        INSERT INTO tasks_history (
            task_id, title, description, status, priority, 
            operation, changed_at
        )
        VALUES (
            OLD.id, OLD.title, OLD.description, OLD.status, 
            OLD.priority, 'DELETE', CURRENT_TIMESTAMP
        );
    END;
