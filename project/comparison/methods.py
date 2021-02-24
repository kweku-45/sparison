
# Algorithm to measure comparison
def perform_match(user1, user2):
    total = 0
    from_user_liked_songs = user1.liked_songs.all()
    to_user_liked_songs = user2.liked_songs.all()
    from_user_liked_songs_count= from_user_liked_songs.count()
    to_user_liked_songs_count = to_user_liked_songs.count()
    total += (to_user_liked_songs_count + from_user_liked_songs_count)
    count = from_user_liked_songs&to_user_liked_songs
    display_count = count.count()
    final = (display_count/total)*100

    return f"Total number of songs scanned through are {total} and your comparison score is {final} %"


# Check if one user is following or not
def check_following1(user1,user2):
    rel = user1.relationships.filter(
        to_people__from_person=user1)
    return rel.filter(pk = user2.id).exists()
     
   
# Check if other user follows back  
def check_following2(user1 , user2):
    rel = user2.relationships.filter(
        to_people__from_person=user2)
    return rel.filter(pk=user1.id).exists()
      
   
    
#Check if two users follow each other
def follow_back(user1, user2):
    return check_following1(user1, user2) and check_following2(user1,user2)
      







    

