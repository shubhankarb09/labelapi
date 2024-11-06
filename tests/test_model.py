from microservice.model import probability_generator

def test_probability_generator_output():
    # Test the types in the returned data
    result = probability_generator("Sample caption text")
    
    assert isinstance(result, dict)  
    for topic, probability in result.items():
        assert isinstance(topic, str)  
        assert isinstance(probability, float) 

def test_probability_generator_topic_count():
    # Test that the function returns between 20 and 100 topics
    result = probability_generator("Sample caption text")
    topic_count = len(result)
    assert 20 <= topic_count <= 100 

def test_probability_generator_probability_sum():
    #Test that the sum of probabilities is approximately 1
    result = probability_generator("Instagram caption")
    total_probability = sum(result.values())
    assert abs(total_probability -1) < 0.01

def test_probability_generator_probability_values():
    #Test that the probability values are between 1 and 0
    result = probability_generator("Instagram caption")
    for probability in result.values():
        assert 0 <= probability <= 1
