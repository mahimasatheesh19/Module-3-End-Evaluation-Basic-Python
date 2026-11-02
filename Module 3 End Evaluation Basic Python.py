feedback_data = {
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': [
' Very GOOD Service!!!',
'poor support, not happy ',
'GREAT experience! will come again.',
'okay okay...',
' not BAD',
'Excellent care, excellent staff!',
'good food and good ambience!',
'Poor response and poor handling of issue',
'Satisfied. But could be better.',
'Good support... quick service.'
],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


new_user = int(input("How many more feedbacks they want to add? "))

for i in range(new_user):
    print("\n Enter details for feedback: ")

    name = input("Enter Name: ")
    feedback = input("Enter Written Feedback: ")
    rating = int(input("Enter Rating (1 - 5): "))

new_S_No = len(feedback_data["S_No"]) + 1

feedback_data["S_No"].append(new_S_No)

feedback_data["Name"].append(name)

feedback_data["Feedback"].append(feedback)

feedback_data["Rating"].append(rating)

print("\nappended feedback_data")

print(feedback_data)

for i in range(len(feedback_data["Feedback"])):

    n_feedback = feedback_data["Feedback"][i]

    n_feedback = n_feedback.replace(".", " ")
    n_feedback = n_feedback.replace(",", " ")
    n_feedback = n_feedback.replace("!", " ")
    n_feedback = n_feedback.replace("?", " ")

    words = n_feedback.split()
    n_feedback = " ".join(words)

    n_feedback = n_feedback.lower()

    feedback_data["Feedback"][i] = n_feedback

print("\cleaned_feedbacks:")

for i in range(len(feedback_data["Feedback"])):
      print(feedback_data["S_No"][i], feedback_data["Name"][i], feedback_data["Feedback"][i])
      
  
def count_word_in_feedbacks(word):
    count = 0

    for n_feedback in feedback_data["Feedback"]:

        n_feedback = n_feedback.lower()
        word = word.lower()

        if word in n_feedback.split():
            count += 1

    return count

print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))

        
print("\final cleaned Feedback Data::")

print(feedback_data)

total_rating = sum(feedback_data["Rating"])
total_feedbacks = len(feedback_data["Rating"])

average_rating = total_rating / total_feedbacks

print("\n average rating:", round(average_rating, 2))

longest_comment = max(feedback_data["Feedback"],key = lambda x: len(x.split()))


longest_word_count = len(longest_comment.split())

print("\n Longest Comment:", longest_comment)
print ("Word Count:", longest_word_count)


unique_word = set()

for n_feedback in feedback_data["Feedback"]:
    words = n_feedback.split()
    unique_word.update(words)
print("\nUnique Words:")
print(sorted(unique_word))


sorted_feedbacks = sorted(zip(
    feedback_data["S_No"], feedback_data["Name"],
    feedback_data["Feedback"], feedback_data["Rating"]),
                          key = lambda x: x[3],
                          reverse = True)

print("\n Feedbacks sorted by Rating:")

for s_no, name, feedback, rating, in sorted_feedbacks:
    print(s_no, name, feedback, rating)

    

