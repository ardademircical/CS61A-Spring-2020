.read sp20data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 
  order by smallest limit 20;

CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color
  from students as first, students as second
  where first.time < second.time and first.pet = second.pet and first.song = second.song;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
