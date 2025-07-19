#!/usr/bin/env python3
"""
Test script for the Daily Task Manager API
Demonstrates the Create Task endpoint
"""

import requests
import json
from datetime import datetime, timedelta

# API base URL
BASE_URL = "http://localhost:8000/api/v1"

def test_create_task():
    """Test the create task endpoint"""
    
    # Task data
    task_data = {
        "title": "Complete project documentation",
        "description": "Write comprehensive API documentation for the Daily Task Manager",
        "priority": "high",
        "due_date": (datetime.now() + timedelta(days=7)).isoformat(),
        "category_id": None
    }
    
    print("Creating task...")
    print(f"Task data: {json.dumps(task_data, indent=2)}")
    
    try:
        response = requests.post(
            f"{BASE_URL}/tasks/",
            json=task_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 201:
            task = response.json()
            print("✅ Task created successfully!")
            print(f"Task ID: {task['id']}")
            print(f"Status: {task['status']}")
            print(f"Created at: {task['created_at']}")
            return task
        else:
            print(f"❌ Failed to create task. Status: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the API. Make sure the server is running on localhost:8000")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_get_tasks():
    """Test the get tasks endpoint"""
    
    print("\nFetching all tasks...")
    
    try:
        response = requests.get(f"{BASE_URL}/tasks/")
        
        if response.status_code == 200:
            tasks_data = response.json()
            print("✅ Tasks retrieved successfully!")
            print(f"Total tasks: {tasks_data['total']}")
            for task in tasks_data['tasks']:
                print(f"- {task['title']} (Priority: {task['priority']}, Status: {task['status']})")
        else:
            print(f"❌ Failed to get tasks. Status: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the API. Make sure the server is running on localhost:8000")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    """Main test function"""
    print("🚀 Testing Daily Task Manager API")
    print("=" * 40)
    
    # Test creating a task
    task = test_create_task()
    
    # Test getting all tasks
    test_get_tasks()
    
    print("\n" + "=" * 40)
    print("✨ Test completed!")

if __name__ == "__main__":
    main() 