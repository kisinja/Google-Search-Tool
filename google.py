from googlesearch import search

def google_search(query, result=5):
    try:
        search_results = search(query, num_results=result)

        print("Search Results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i+1}. {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    query = input("Enter the search query: ")
    google_search(query)