import queue
import uuid
import time
import random

# Global queue for requests
request_queue = queue.Queue()

def generate_request():
    """Generate a new request and add it to the queue"""
    request_id = str(uuid.uuid4())[:8]  # Short unique ID
    request_data = {
        'id': request_id,
        'timestamp': time.time(),
        'description': f'Service request {request_id}'
    }
    request_queue.put(request_data)
    print(f"Generated request: {request_data['description']}")

def process_request():
    """Process a request from the queue if available"""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing request: {request['description']}")
        # Simulate processing time
        time.sleep(0.5)
        print(f"Completed request: {request['id']}")
    else:
        print("Queue is empty, no requests to process")

def main():
    """Main program loop"""
    print("Request Processing System")
    print("Commands: 'g' - generate request, 'p' - process request, 'q' - quit")
    
    while True:
        # Auto-generate requests randomly (30% chance)
        if random.random() < 0.3:
            generate_request()
        
        # Get user command
        command = input("\nEnter command (g/p/q): ").lower().strip()
        
        if command == 'g':
            generate_request()
        elif command == 'p':
            process_request()
        elif command == 'q':
            print("Shutting down system...")
            # Process remaining requests
            while not request_queue.empty():
                process_request()
            break
        else:
            print("Invalid command. Use 'g', 'p', or 'q'")

if __name__ == "__main__":
    main()