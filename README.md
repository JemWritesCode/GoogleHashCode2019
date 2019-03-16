# GoogleHashCode2019
Code from the Google Hash Code competition in 2019

Score 0 - Incomplete

4 hours with a team of 3. My first time participating in a coding competition, and it was a lot of fun! I learned a lot! We went with Python so we could put a solution together quickly. This was a good choice, but none of us have extensive expreience with it and it was my first time working with Python. We had a lot of pseduo code on paper that we didn't quite know how to implement-- in hindsight maybe we should have started coding sooner so we could at least have an output file instead of spending so much time on algorithm design. Still I think we did pretty well all things considered and we came pretty close to having an output file.

We didn't finish, but our idea was to basically come up with a difference score that was based on absolute value (distance from 0.) Photos that were TOO different would end up furhter in the negatives, and photos that were TOO similar would end up having a high positive number. A low absolute value between two photos would mean they would end up with a high interest factor. 

For what we have so far we read each line into an array. We add the photoID as the last item in the array with ` picture += " " + str(i)`.  Then we sort Horizontal  & vertical into different lists. All the vertical photos that are now in order by number of tags then get paired off into slides. We wanted to intially sort by number of tags per slide -- this would get our difference scores generally closer to 0 for all photos. `slide_tag_total += int(picture[1])` adds the number of tags in each slide to the slide array. We were planning to at least sort slides by number of tags but we ran out of time.

