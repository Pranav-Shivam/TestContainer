from router.neuralSearch import NeuralSearcher
def searchResult(cityName):
    # Create an instance of the neural searcher
    neural_searcher = NeuralSearcher(collection_name='startups')
    response=neural_searcher.search(str(cityName))
    for city in response:
        print(city["city"])
    return response

