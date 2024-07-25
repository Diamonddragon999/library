-- SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
-- SET AUTOCOMMIT = 0;
-- START TRANSACTION;
-- SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms_main_database`
--
CREATE DATABASE lms_main_database;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

USE lms_main_database;

CREATE TABLE `admin` (
  `id` int NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`) VALUES
(1, 'admin@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `author` varchar(255) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `edition` varchar(255) NOT NULL,
  `count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `name`, `description`, `author`, `availability`, `edition`, `count`) VALUES
(1, 'Clean Code', 'A handbook of agile software craftsmanship', 'Robert C. Martin', 1, 'First Edition', 5),
(2, 'The Pragmatic Programmer', 'Your journey to mastery', 'Andrew Hunt, David Thomas', 1, '20th Anniversary Edition', 3),
(3, 'Design Patterns', 'Elements of Reusable Object-Oriented Software', 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 1, 'First Edition', 2),
(4, 'Introduction to Algorithms', 'A comprehensive update of the leading algorithms text', 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein', 1, 'Third Edition', 4),
(5, 'Code Complete', 'A practical handbook of software construction', 'Steve McConnell', 1, 'Second Edition', 3),
(6, 'The Mythical Man-Month', 'Essays on Software Engineering', 'Frederick P. Brooks Jr.', 0, 'Anniversary Edition', 0),
(7, 'Cracking the Coding Interview', '189 Programming Questions and Solutions', 'Gayle Laakmann McDowell', 1, '6th Edition', 5),
(8, 'Head First Design Patterns', 'A Brain-Friendly Guide', 'Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra', 1, 'Second Edition', 2),
(9, 'Database System Concepts', 'Fundamentals of database systems', 'Abraham Silberschatz, Henry F. Korth, S. Sudarshan', 1, '7th Edition', 3),
(10, 'Computer Networks', 'A comprehensive introduction to computer networks', 'Andrew S. Tanenbaum, David J. Wetherall', 1, '5th Edition', 1),
(11, 'Artificial Intelligence: A Modern Approach', 'Comprehensive introduction to AI', 'Stuart Russell, Peter Norvig', 1, '4th Edition', 3),
(12, 'The C Programming Language', 'Classic book on C programming', 'Brian W. Kernighan, Dennis M. Ritchie', 1, '2nd Edition', 2),
(13, 'JavaScript: The Good Parts', 'Unearthing the excellence in JavaScript', 'Douglas Crockford', 1, '1st Edition', 4),
(14, 'Python Crash Course', 'A hands-on, project-based introduction to programming', 'Eric Matthes', 1, '2nd Edition', 5),
(15, 'Operating System Concepts', 'Fundamental concepts of operating systems', 'Abraham Silberschatz, Peter B. Galvin, Greg Gagne', 1, '10th Edition', 2),
(16, 'Refactoring', 'Improving the design of existing code', 'Martin Fowler', 1, '2nd Edition', 3),
(17, 'The Art of Computer Programming', 'Comprehensive monograph on computer programming', 'Donald E. Knuth', 0, '1st Edition', 0),
(18, 'Designing Data-Intensive Applications', 'The big ideas behind reliable, scalable, and maintainable systems', 'Martin Kleppmann', 1, '1st Edition', 4),
(19, 'Clean Architecture', 'A craftsman''s guide to software structure and design', 'Robert C. Martin', 1, '1st Edition', 2),
(20, 'You Don''t Know JS', 'A book series on JavaScript', 'Kyle Simpson', 1, '2nd Edition', 3),
(21, 'Compilers: Principles, Techniques, and Tools', 'Comprehensive compiler design textbook', 'Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman', 1, '2nd Edition', 1),
(22, 'Data Science for Business', 'What you need to know about data mining and data-analytic thinking', 'Foster Provost, Tom Fawcett', 1, '1st Edition', 3),
(23, 'Learning Python', 'Powerful Object-Oriented Programming', 'Mark Lutz', 1, '5th Edition', 4),
(24, 'Web Development with Node and Express', 'Leveraging the JavaScript Stack', 'Ethan Brown', 1, '2nd Edition', 2),
(25, 'Eloquent JavaScript', 'A modern introduction to programming', 'Marijn Haverbeke', 1, '3rd Edition', 3),
(26, 'Machine Learning', 'A probabilistic perspective', 'Kevin P. Murphy', 0, '1st Edition', 0),
(27, 'The DevOps Handbook', 'How to Create World-Class Agility, Reliability, and Security in Technology Organizations', 'Gene Kim, Patrick Debois, John Willis, Jez Humble', 1, '1st Edition', 2),
(28, 'Cybersecurity and Cyberwar', 'What Everyone Needs to Know', 'P.W. Singer, Allan Friedman', 1, '1st Edition', 1),
(29, 'The Phoenix Project', 'A Novel about IT, DevOps, and Helping Your Business Win', 'Gene Kim, Kevin Behr, George Spafford', 1, '1st Edition', 3),
(30, 'Algorithms to Live By', 'The Computer Science of Human Decisions', 'Brian Christian, Tom Griffiths', 1, '1st Edition', 2);
-- --------------------------------------------------------

--
-- Table structure for table `reserve`
--

CREATE TABLE `reserve` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reserve`
--

-- INSERT INTO `reserve` (`id`, `user_id`, `book_id`) VALUES
-- (1, 1, 1),
-- (2, 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--
SET GLOBAL max_allowed_packet=268435456;
SET GLOBAL innodb_log_file_size = 134217728;


CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(1000) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `bio` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT "",
  `mob` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT "",
  `lock` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted` tinyint(1) not NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `bio`, `mob`, `lock`, `created_at`, `deleted`) VALUES
(1, 'John Doe', 'john.doe@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Software engineer with 5 years of experience.', '1234567890', 0, '2024-07-16 10:00:00', 1),
(2, 'Jane Smith', 'jane.smith@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Marketing specialist passionate about digital strategies.', '2345678901', 0, '2024-07-16 10:15:00', 0),
(3, 'Mike Johnson', 'mike.johnson@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Freelance graphic designer with a keen eye for detail.', '3456789012', 0, '2024-07-16 10:30:00', 0),
(4, 'Emily Brown', 'emily.brown@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Passionate teacher specializing in elementary education.', '4567890123', 0, '2024-07-16 10:45:00', 0),
(5, 'David Lee', 'david.lee@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Financial analyst with expertise in market trends.', '5678901234', 0, '2024-07-16 11:00:00', 0),
(6, 'Sarah Wilson', 'sarah.wilson@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Registered nurse dedicated to patient care.', '6789012345', 0, '2024-07-16 11:15:00', 0),
(7, 'Tom Taylor', 'tom.taylor@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Aspiring chef with a passion for fusion cuisine.', '7890123456', 0, '2024-07-16 11:30:00', 0),
(8, 'Lisa Anderson', 'lisa.anderson@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Environmental scientist  focused on sustainable practices.', '8901234567', 0, '2024-07-16 11:45:00', 0),
(9, 'Chris Martinez', 'chris.martinez@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Fitness trainer specializing in HIIT workouts.', '9012345678', 0, '2024-07-16 12:00:00', 0),
(10, 'Emma Davis', 'emma.davis@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Freelance writer covering technology and innovation.', '0123456789', 0, '2024-07-16 12:15:00', 0),
(11, 'Ryan White', 'ryan.white@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Civil engineer with a focus on urban planning.', '1234567890', 0, '2024-07-16 12:30:00', 0),
(12, 'Olivia Harris', 'olivia.harris@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Social media manager with a creative flair.', '2345678901', 0, '2024-07-16 12:45:00', 0),
(13, 'Daniel Clark', 'daniel.clark@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Veterinarian specializing in exotic animals.', '3456789012', 0, '2024-07-16 13:00:00', 0),
(14, 'Sophia Lewis', 'sophia.lewis@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Psychologist focusing on cognitive behavioral therapy.', '4567890123', 0, '2024-07-16 13:15:00', 0),
(15, 'Andrew Robinson', 'andrew.robinson@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Mechanical engineer working in the automotive industry.', '5678901234', 0, '2024-07-16 13:30:00', 0),
(16, 'Grace Walker', 'grace.walker@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Yoga instructor promoting mindfulness and well-being.', '6789012345', 0, '2024-07-16 13:45:00', 0),
(17, 'Kevin Hall', 'kevin.hall@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Data scientist specializing in machine learning algorithms.', '7890123456', 0, '2024-07-16 14:00:00', 0),
(18, 'Natalie Young', 'natalie.young@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Interior designer with a passion for sustainable materials.', '8901234567', 0, '2024-07-16 14:15:00', 0),
(19, 'Jason Scott', 'jason.scott@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Professional photographer specializing in wildlife.', '9012345678', 0, '2024-07-16 14:30:00', 0),
(20, 'Rachel Green', 'rachel.green@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Human resources manager focused on employee development.', '0123456789', 0, '2024-07-16 14:45:00', 0),
(21, 'Mark Thompson', 'mark.thompson@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Architect with a focus on eco-friendly design.', '1234567890', 0, '2024-07-16 15:00:00', 0),
(22, 'Jessica Parker', 'jessica.parker@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Event planner specializing in corporate conferences.', '2345678901', 0, '2024-07-16 15:15:00', 0),
(23, 'Brian Adams', 'brian.adams@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Sales manager with expertise in B2B relationships.', '3456789012', 0, '2024-07-16 15:30:00', 0),
(24, 'Michelle Turner', 'michelle.turner@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Nutritionist promoting plant-based diets.', '4567890123', 0, '2024-07-16 15:45:00', 0),
(25, 'Paul Evans', 'paul.evans@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Electrician specializing in renewable energy systems.', '5678901234', 0, '2024-07-16 16:00:00', 0),
(26, 'Karen Nelson', 'karen.nelson@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Librarian passionate about literacy programs.', '6789012345', 0, '2024-07-16 16:15:00', 0),
(27, 'Steven Carter', 'steven.carter@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Cybersecurity analyst with expertise in threat detection.', '7890123456', 0, '2024-07-16 16:30:00', 0),
(28, 'Laura Mitchell', 'laura.mitchell@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Travel blogger exploring off-the-beaten-path destinations.', '8901234567', 0, '2024-07-16 16:45:00', 0),
(29, 'Robert Phillips', 'robert.phillips@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Product manager in the tech startup scene.', '9012345678', 0, '2024-07-16 17:00:00', 0),
(30, 'Amy Cooper', 'amy.cooper@boot.camp', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Musician and music teacher specializing in piano.', '0123456789', 0, '2024-07-16 17:15:00', 0);
--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reserve`
--
ALTER TABLE `reserve`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `reserve`
--
ALTER TABLE `reserve`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;
ALTER USER 'root'@'%' IDENTIFIED BY 'lms_admin_123';
GRANT ALL PRIVILEGES on *.* to 'root'@'%';
CREATE USER 'lms_user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'lms_user'@'%';
FLUSH PRIVILEGES;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
