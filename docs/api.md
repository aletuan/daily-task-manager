# API Documentation

## Overview

This document provides comprehensive API documentation for the Daily Task Manager backend.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All API endpoints require authentication using JWT tokens.

### Headers
```
Authorization: Bearer <your-jwt-token>
Content-Type: application/json
```

## Endpoints

### Tasks

#### GET /tasks
Retrieve all tasks for the authenticated user.

**Response:**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete project documentation",
      "description": "Write comprehensive API docs",
      "priority": "high",
      "status": "in_progress",
      "due_date": "2024-01-15",
      "created_at": "2024-01-01T10:00:00Z",
      "updated_at": "2024-01-01T10:00:00Z"
    }
  ]
}
```

#### POST /tasks
Create a new task.

**Request Body:**
```json
{
  "title": "New task",
  "description": "Task description",
  "priority": "medium",
  "due_date": "2024-01-15"
}
```

#### PUT /tasks/{task_id}
Update an existing task.

#### DELETE /tasks/{task_id}
Delete a task.

### Categories

#### GET /categories
Retrieve all categories.

#### POST /categories
Create a new category.

### Users

#### POST /auth/login
Authenticate user and receive JWT token.

#### POST /auth/register
Register a new user.

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Validation error",
  "errors": [
    {
      "field": "title",
      "message": "Title is required"
    }
  ]
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid authentication credentials"
}
```

### 404 Not Found
```json
{
  "detail": "Task not found"
}
```

## Rate Limiting

API requests are limited to 100 requests per minute per user.

## Versioning

API versioning is handled through the URL path: `/api/v1/` 