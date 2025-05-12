from app import verify_identity

def test_verification():
    # Replace these paths with your actual image paths
    id_card_path = "test_id.jpg"
    webcam_image_path = "test_webcam.jpg"
    
    try:
        result = verify_identity(id_card_path, webcam_image_path)
        print("Verification Result:")
        print(result)
    except Exception as e:
        print(f"Error during verification: {e}")

if __name__ == "__main__":
    test_verification() 