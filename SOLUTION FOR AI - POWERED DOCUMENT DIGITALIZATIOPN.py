def classify_documents(documents):
    # Define keywords for each category
    categories = {
        "Legal": ["court", "legal", "lawsuit"],
        "Financial": ["budget", "financial", "invoice", "payment"],
        "Personnel": ["employee", "HR", "contract"],
    }
    
    results = []
    
    for doc in documents:
        found_category = "Miscellaneous"  # Default category
        for category, keywords in categories.items():
            if any(keyword in doc.lower() for keyword in keywords):
                found_category = category
                break
        results.append(found_category)
    
    return results

# Read input from stdin
def main():
    # Custom input for testing purposes
    custom_input = [
        "3",  # Number of documents
        "This is an official court document.",  # Document 1
        "The annual budget was approved last month.",  # Document 2
        "HR policies for new employees."  # Document 3
    ]
    
    # Simulating input reading
    n = int(custom_input[0])
    documents = custom_input[1:n + 1]  # Grab the documents based on input count
    
    # Get the classification results
    results = classify_documents(documents)
    
    # Output each result on a new line
    for result in results:
        print(result)
    
    # Print team details
    print("Team Name: DevOps Ninjas")
    print("Member 1: Sayan Som")
    print("Member 2: Shankha Shubhra Chatterjee")
    print("Member 3: Sayan Tarafdar")

# Call the main function to execute the classification
if _name_ == "_main_":
    main()