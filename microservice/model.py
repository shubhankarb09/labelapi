import numpy as np
import random

#Generates dummy probabilities
def probability_generator(text:str):
    labels = [
    "Photography", "Fashion", "Beauty", "Travel", "Food", "Art", "Nature",
    "Fitness", "Health", "Home Decor", "DIY", "Pets", "Family", "Self-care",
    "Music", "Movies", "Celebrities", "Humor", "Gaming", "Books",
    "News", "Social Causes", "Holidays", "Sports", "Entrepreneurship",
    "Career", "Technology", "Artificial Intelligence", "Cybersecurity",
    "Love", "Selfies", "Positivity", "Nostalgia", "Daily Life", "Sunset",
    "Wanderlust", "Cooking", "OOTD", "Gym", "Makeup", "Design", "Motivation",
    "Wellness", "Yoga", "Skincare", "Haircare", "Streetwear", "Luxury",
    "Sustainability", "Vegan", "Organic", "Mindfulness", "Meditation",
    "Mental Health", "Parenting", "Education", "Science", "Space",
    "Environment", "Climate Change", "Recycling", "Minimalism", "Gardening",
    "Interior Design", "Architecture", "Crafts", "Painting", "Drawing",
    "Sculpture", "Street Art", "Fashion Week", "Beauty Hacks", "Travel Tips",
    "Restaurant Reviews", "Recipes", "Cocktails", "Wine", "Beer",
    "Coffee", "Tea", "Smoothies", "Workouts", "Running", "Cycling",
    "Swimming", "Hiking", "Camping", "Beach", "Mountains", "City Life",
    "Rural Life", "Festivals", "Concerts", "Theater", "Dance", "Poetry",
    "Writing", "Podcasts", "Startups", "Investing", "Personal Finance",
    "Cryptocurrency", "Robotics", "Virtual Reality", "Augmented Reality"]
    #Since business requirement is to have minimum of 20 topics
    label_count = random.randrange(20, len(labels))
    print(label_count)
    labels_rand = random.sample(labels, label_count)


    list_probabilities = {topic: random.uniform(0,1) for topic in labels_rand}
    total = sum(list_probabilities.values())

    return {k: v/total for k, v in list_probabilities.items()}
   