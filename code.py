import hashlib

class DigitalIdentity:
    def __init__(self, full_name, id_number, password):
        self.full_name = full_name  # Store the user's full name
        self.id_number = id_number  # Store the user's identification number
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password for storage
        self.id = hashlib.sha256(id_number.encode()).hexdigest()  # Generate a unique hash ID from the identification number

class EPetition:
    def __init__(self):
        self.petitions = {}  # Dictionary to store petitions
        self.signatures = {}  # Dictionary to store signatures for each petition

    def create_petition(self, title, description, creator):
        # Create a petition and generate a unique ID based on content
        petition_content = f"{title}{description}{creator.id}".encode('utf-8')
        petition_id = hashlib.sha256(petition_content).hexdigest()
        self.petitions[petition_id] = {
            "title": title,
            "description": description,
            "creator": creator,
            "signature_count": 0
        }
        self.signatures[petition_id] = set()
        print(f"Petition successfully created: {petition_id}")

    def list_petitions(self):
        # List all available petitions
        if not self.petitions:
            print("No petitions available.")
            return None
        print("Available Petitions:")
        petition_ids = []
        for index, (petition_id, details) in enumerate(self.petitions.items(), 1):
            print(f"{index}. ID: {petition_id}, Title: {details['title']}, Signatures: {details['signature_count']}")
            petition_ids.append(petition_id)
        return petition_ids

    def sign_petition(self, petition_id, signer):
        # Sign a petition if not already signed by the user
        if signer.id in self.signatures[petition_id]:
            print("You have already signed this petition.")
            return
        self.signatures[petition_id].add(signer.id)
        self.petitions[petition_id]["signature_count"] += 1
        print("Petition successfully signed.")