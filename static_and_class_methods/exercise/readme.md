# Photo Album
Create a class called PhotoAlbum. Upon initialization, it should receive pages (int). It should also have one more attribute: photos (empty matrix) representing the album with its pages where you should put the photos. Each page can contain only 4 photos.
The class should also have 3 more methods:
- from_photos_count(photos_count: int) - creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos.
- add_photo(label:str) - adds the photo in the first possible page and slot and return "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}". If there are no free slots left, return "No more free slots"
- display() - returns a string representation of each page and the photos in it. Each photo is marked with "[]", and the page separation is made using 11 dashes (-). For example, if we have 1 page and 2 photos:
    "-----------"
    
    [] []

    "-----------"
    
    and if we have 2 empty pages:
    
    "-----------"
    
    "-----------"
    
    "-----------"


# Movie World
Create the following project structure

![image](https://user-images.githubusercontent.com/104040753/200648964-ce32e1e5-33bb-4c99-b96b-2330527c5da8.png)

### Class Customer
Upon initialization, the Customer class should receive the following parameters: name: str, age: int, id: int. Each customer should also have an instance attribute called rented_dvds (empty list with DVD instances).
Implement the __repr__ method, so it returns the following string: "{id}: {name} of age {age} has {count_rented_dvds} rented DVD's ({dvd_names joined by comma and space})"

### Class DVD
Upon initialization, the DVD class should receive the following parameters: name: str, id: int, creation_year: int, creation_month: str, age_restriction: int. Each DVD should also have an attribute called is_rented (False by default)
Create a method called from_date(id: int, name: str, date: str, age_restriction: int) - it should create a new instance using the provided data. The date will be in the format "day.month.year" - all of them should be numbers.
Implement the __repr__ method so it returns the following string: "{id}: {name} ({creation_month} {creation_year}) has age restriction {age_restriction}. Status: {rented/not rented}"

### Class MovieWorld
The MovieWorld class should receive one parameter upon initialization: name: str. Each MovieWorld instance should also have 2 more attributes: customers (empty list of Customer objects), dvds (empty list of DVD objects). The class should also have the following methods:
- dvd_capacity() - returns 15 - the DVD capacity of a movie world
- customer_capacity() - returns 10 - the customer capacity of a movie world
- add_customer(customer: Customer) - add the customer if capacity not exceeded
- add_dvd(dvd: DVD) - add the DVD if capacity not exceeded
- rent_dvd(customer_id: int, dvd_id: int)
    - If the customer has already rented that DVD return "{customer_name} has already rented {dvd_name}"
    - If the DVD is rented by someone else, return "DVD is already rented"
    - If the customer is not allowed to rent the DVD, return "{customer_name} should be at least {dvd_age_restriction} to rent this movie"
    - Otherwise, the rent is successful (the DVD is rented and added to the customer's DVDs). Return "{customer_name} has successfully rented {dvd_name}"
- return_dvd(customer_id, dvd_id) - if the DVD is in the customer, he/she should return it and the method should return the message "{customer_name} has successfully returned {dvd_name}". Otherwise, return "{customer_name} does not have that DVD" 
- __repr__() - return the string representation of each customer and each DVD on separate lines
<<<<<<< HEAD


# Document Management
Create the following project structure



### Class Topic
The Topic class should receive the following parameters upon initialization: id: int, topic: str, storage_folder: str. It should have two methods:
- edit(new_topic: str, new_storage_folder: str) - change the topic and the storage folder
- __repr__() - returns a string representation of the topic in the format: "Topic {id}: {topic} in {storage_folder}"

### Class Category
The Category class should receive the following parameters upon initialization: id: int, name: str. The class should have two methods:
- edit(new_name: str) - edit the name of the category
- __repr__() - returns a string representation of the category in the following format: "Category {id}: {name}"

### Class Document
The Document class should receive the following parameters upon initialization: id: int, category_id: int, topic_id: int, file_name: str. The class should also have one more attribute called tags (empty list). The class should also have 4 methods:
- from_instances(id: int, category: Category, topic: Topic, file_name: str) - create a new instance using the provided category and topic instances
- add_tag(tag_content: str) - if the tag is not already in the tags list, add it to the tags list
- remove_tag(tag_content:str) - if the tag is in the tags list, delete it
- edit(file_name: str) - change the file name with the given one
- __repr__() - returns a string representation of a document in the format: "Document {id}: {file_name}; category {category_id}, topic {topic_id}, tags: {tags joined by comma and space)}"

### Class Storage
Upon initialization the class Storage will not receive any parameters. It should have 3 instance attributes: categories (empty list), topics (empty list), documents (empty list). The class should have the following methods:
- add_category(category:Category) - add the category if it is not in the list
- add_topic(topic:Topic) - add the topic if it does not exist
- add_document(document:Document) - add the document if it does not exist
- edit_category(category_id: int, new_name:str) - edit the name of the category with the provided id
- edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) - edit the topic with the given id
- edit_document(document_id: int, new_file_name: str) - edit the document with the given id
- delete_category(category_id) - delete the category with the provided id
- delete_topic(topic_id) - delete the topic with the provided id
- delete_document(document_id) - delete the document with the provided id
- get_document(document_id) - return the document with the provided id
- __repr__() - returns a string representation of each document on separate lines
=======
>>>>>>> b64767828143efb374c8a3827bf190bfa7fb20d1
