import pandas as pd

# Data
data = {
    "query": [
        "What is AI?",
        "How does BERT work?",
        "What is Machine Learning?",
        "Who invented BERT?",
        "Define natural language processing.",
        "What is deep learning?",
        "What is the weather like today?",
        "How can I use Python for AI?",
        "What is reinforcement learning?",
        "What is a chatbot?",
        "Explain supervised learning.",
        "Explain unsupervised learning.",
        "What is transfer learning?",
        "What does NLP stand for?",
        "What is the use of transformers in AI?",
        "How does a neural network work?",
        "What is overfitting?",
        "What is underfitting?",
        "What is a dataset?",
        "What is the difference between AI and Machine Learning?",
        # Additional Queries
        "What are the types of AI?",
        "Who is considered the father of AI?",
        "What is the Turing Test?",
        "What are some applications of AI in daily life?",
        "Can AI be creative?",
        "What is AI-generated art?",
        "What games use AI technology?",
        "Explain the concept of self-driving cars.",
        "How do recommendation systems work?",
        "What is the primary goal of AI research?",
        "What is the most popular programming language for AI?",
        "What are the ethical concerns surrounding AI?",
        "What is a fun fact about AI?",
        "How can AI help in climate change?",
        "What’s a robot’s favorite type of music?",
        "Can robots dance?",
        "Has AI ever beaten a human in a game?",
        "What is the future of AI in education?",
        "What's the craziest application of AI you've heard?",
        "If AI could have a personality, what would it be like?",
        "Can you tell me an AI joke?",
        "What is the best way to celebrate AI Day?",
        "How does AI relate to space exploration?",
        "Is AI going to take over the world?",
        "Can AI create music?",
        "What are some humorous AI fails?",
         # Additional Queries
         "What is a computer?",
        "Define algorithms.",
        "What is the purpose of data structures?",
        "What is the difference between a list and an array?",
        "What is recursion?",
        "Explain the concept of object-oriented programming.",
        "What is the difference between a compiler and an interpreter?",
        "What is big O notation?",
        "What are sorting algorithms?",
        "What is cloud computing?",
        "What is a database?",
        "What is SQL?",
        "What are the types of databases?",
        "What is machine learning?",
        "What is an API?",
        "What is the Internet of Things (IoT)?",
        "What is cybersecurity?",
        "Explain the concept of a software development lifecycle.",
        "What are the different types of programming languages?",
        "What is open-source software?",
        "What is version control?",
        "What is a stack and a queue?",
        "What is artificial intelligence?",
        "What is a hash table?",
        "What is a variable in programming?",
        "What are loops in programming?",
        "Explain the concept of multithreading.",
        "What is a bug in software development?",
        "What are the main components of a computer?",
        "What is a network?",
        "What is the difference between RAM and ROM?",
        "What is a software framework?",
        "What is a web server?",
        "What is encryption?",
        "What are the basic principles of software engineering?",
        "What is debugging?",
        "What is the difference between front-end and back-end development?",
        "What is a content management system (CMS)?",
        "What is data mining?",
        "Explain cloud storage.",
        "What is a software library?",
        "What is the difference between IPv4 and IPv6?",
        "What is a pixel?",
        "What does DNS stand for?",
        "What is machine learning vs deep learning?",
        "What is a computer network?",
        "What is blockchain technology?",
        "What are the advantages of using algorithms?",
        "What is the difference between HTTP and HTTPS?",
        "What are chatbots?",
        "What is gamification in software design?",
        "Explain what a macro is in programming.",
        "What is a user interface (UI)?",
        "What is an operating system?",
        "What is recursion vs iteration?",
        "What are the ethical implications of computer science?",
        "What are some careers in computer science?",
        "What is a neural network?",
        "What is augmented reality (AR)?",
        "What is virtual reality (VR)?",
        "What is quantum computing?",
        "What is the Turing machine?",
        "Explain the concept of data visualization.",
        "What is a data warehouse?",
        "what is significance if cloud computing",
        "What is a mechanical computer?",
        "What is the Analytical Engine?",
        "Who is known as the first computer programmer?",
        "What is ENIAC?",
        "What was the purpose of the ENIAC?",
        "What are vacuum tubes?",
        "What are transistors?",
        "What are integrated circuits?",
        "What is the microprocessor?",
        "Who invented the microprocessor?",
        "What is the significance of the IBM PC?",
        "What is Moore's Law?",
        "When was the first programming language developed?",
        "What is FORTRAN?",
        "What is COBOL?",
        "Who invented the World Wide Web?",
        "What was the first computer virus?",
        "What is the role of ARPANET in computer history?",
        "What is the significance of UNIX?",
        "What was the first personal computer?",
        "What is the role of Apple in computer history?",
        "What is a graphical user interface (GUI)?",
        "What is the Turing Machine?",
        "What is binary code?",
        "What is the Von Neumann architecture?",
        "What is the significance of punch cards?",
        "Who invented the first laptop?",
        "What is the role of Microsoft in computer history?",
        "What is the history of computer networking?",
        "What is the difference between analog and digital computers?",
        "What is a mainframe computer?",
        "What is the role of Linux in computer history?",
        "What is cloud computing?",
        "What is the history of supercomputers?",
        "What is quantum computing?",
        "What is the role of AI in modern computers?",
        "What is the significance of the Macintosh?",
        "What is a supercomputer?",
        "What is the role of Python in computer history?",
        "What is the significance of Java?",
        "What are the contributions of Alan Turing?",
        "What is the history of punch cards?",
        "What is a minicomputer?",
        "What is the significance of the Intel 8080?",
        "What is the difference between a compiler and an interpreter?",
        "What is the significance of BASIC?",
        "What is the history of the hard drive?",
        "What is a wearable computer?",
        "What is a personal digital assistant (PDA)?",
        "What is virtual memory?",
        "What is a server?",
        "What is the history of database management systems?",
        "Who is Vannevar Bush?",
        "What is the difference between ROM and RAM?",
        "What is the significance of the Macintosh 128K?",
        "What is the history of video games in computing?",
        "What is the significance of the Babbage Difference Engine?",
        "What is the history of artificial intelligence?",
        "What is ASCII art?",
        "What are Boolean logic and its role in computing?",
        "What is computer vision?",
        "What is the significance of the Commodore 64?",
        "What is the history of graphical processing units (GPUs)?",
        "What is packet switching?",
        "What is the history of email?",
        "What is the role of open-source in computer history?",
        "What is the history of USB technology?",
        "What is the significance of the Internet of Things (IoT)?",
        "What is edge computing?",
        "What is the significance of wearable technology?",
        "What is the history of open-source software?",
        "What is the history of computers?",
        "Who are some pioneers of computing?",
        "What are the generations of computers?",
        "What is the purpose of a computer?",
        "What was the first use of computers?",
        "How has computing impacted society?",
        "What are the major milestones in computer history?",
        "What is the impact of the internet on computing?",
        "How did programming evolve?",
        "What are some key developments in hardware?",
        "What role did World War II play in computer history?",
        "What is the difference between analog and digital computers?",
        "What is the role of open-source in computer history?",
        "How have computers become more accessible?",
        "What is the significance of artificial intelligence in computing?",
        "What is the role of universities in computer history?",
        "What are some early uses of computers in business?",
        "What is the impact of mobile computing?",
        "What is the history of human-computer interaction?",
        "What is the significance of cloud computing?"
    ],
    "response": [
        "AI stands for Artificial Intelligence. It enables machines to perform tasks that typically require human intelligence.",
        "BERT uses a transformer architecture to understand the context of words in a bidirectional manner.",
        "Machine Learning is a subset of AI where systems learn from data and improve over time without being explicitly programmed.",
        "BERT was introduced by researchers at Google in 2018.",
        "Natural language processing is a branch of AI that focuses on enabling machines to understand and generate human language.",
        "Deep learning is a subset of Machine Learning that uses neural networks with many layers to analyze data.",
        "I'm not sure about the weather. Please check your local forecast.",
        "Python is widely used in AI for libraries like TensorFlow, PyTorch, and scikit-learn, which simplify model development.",
        "Reinforcement learning is a type of Machine Learning where an agent learns by interacting with its environment and receiving rewards or penalties.",
        "A chatbot is an AI program designed to simulate human conversation and respond to user inputs.",
        "Supervised learning is a Machine Learning technique where the model is trained on labeled data.",
        "Unsupervised learning is a Machine Learning technique where the model identifies patterns in data without labeled outputs.",
        "Transfer learning is a Machine Learning method where a pre-trained model is adapted to a new, related task.",
        "NLP stands for Natural Language Processing.",
        "Transformers are used in AI to process sequences of data, such as text, for tasks like translation and summarization.",
        "A neural network processes data through layers of interconnected nodes that simulate the behavior of the human brain.",
        "Overfitting occurs when a model learns noise in the training data and performs poorly on new data.",
        "Underfitting occurs when a model fails to capture the underlying patterns in the data.",
        "A dataset is a collection of data points used to train, validate, and test Machine Learning models.",
        "AI is the broader field, while Machine Learning is a subset focused on enabling machines to learn from data.",
        # Additional Responses
        "The main types of AI are narrow AI, general AI, and superintelligent AI.",
        "Alan Turing is often considered the father of AI.",
        "The Turing Test measures a machine's ability to exhibit intelligent behavior equivalent to or indistinguishable from that of a human.",
        "AI is used in daily life for virtual assistants, customer service chatbots, and personalized recommendations.",
        "AI can indeed be creative! Some AI models generate artwork and music.",
        "AI-generated art uses algorithms to create visual art, often based on learned styles.",
        "Games like Chess, Go, and various video games utilize AI technology for opponents.",
        "Self-driving cars use AI to interpret data from sensors and navigate roads safely.",
        "Recommendation systems analyze user data to suggest products, films, or content the user might enjoy.",
        "The primary goal of AI research is to create systems that can perform tasks that typically require human intelligence.",
        "Python is often considered the most popular programming language for AI.",
        "Ethical concerns surrounding AI include privacy, bias, and the potential for job displacement.",
        "A fun fact about AI is that it can predict your next word while texting!",
        "AI can analyze climate data to model future scenarios and suggest solutions.",
        "What’s a robot’s favorite type of music? Heavy metal!",
        "Yes, some robots can be programmed to dance and perform choreographed movements!",
        "Yes, AI has beat world champions in games like Chess and Go.",
        "AI has the potential to personalize learning experiences and assist educators.",
        "The craziest application of AI might be using it to write scripts for Hollywood movies!",
        "If AI had a personality, it might be analytical, inspirational, and a bit quirky!",
        "Why did the AI go to therapy? It had too many complex variables!",
        "You can celebrate AI Day by trying out AI tools or learning about AI advancements.",
        "AI helps in space exploration by analyzing vast amounts of data and assisting in navigation.",
        "There's a lot of debate about that, but for now, it's about collaboration, not domination!",
        "Yes, AI can generate music based on patterns learned from existing songs.",
        "Some AI systems have struggled with simple tasks or produced unexpected results, leading to comical outcomes.",
        # Additional Responses
        "A computer is an electronic device that processes data and performs logical operations according to a set of instructions.",
        "An algorithm is a step-by-step procedure for solving a problem or accomplishing a task.",
        "Data structures are specific formats for organizing and storing data to enable efficient access and modification.",
        "A list is a built-in data type in Python that can change in size, while an array is a static data structure with a fixed size.",
        "Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem.",
        "Object-oriented programming (OOP) is a programming paradigm based on the concept of 'objects' that contain data and methods.",
        "A compiler translates the entire source code into machine code before execution, whereas an interpreter translates code line-by-line.",
        "Big O notation is a mathematical representation that describes the limiting behavior of a function, providing an upper bound on performance.",
        "Sorting algorithms are methods for arranging the elements of a list or array in a certain order.",
        "Cloud computing delivers computing services over the internet, including storage, processing, and networking.",
        "A database is a structured collection of data that is stored and accessed electronically.",
        "SQL (Structured Query Language) is a programming language used to manage and manipulate relational databases.",
        "Types of databases include relational, NoSQL, distributed, and graph databases.",
        "Machine learning is a subset of AI focused on developing algorithms that allow computers to learn from and make predictions based on data.",
        "An API (Application Programming Interface) allows different software applications to communicate with each other.",
        "The Internet of Things (IoT) refers to a network of physical devices connected to the internet that can collect and exchange data.",
        "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks.",
        "The software development lifecycle (SDLC) is a process for planning, creating, testing, and deploying software applications.",
        "The main types of programming languages include procedural, object-oriented, functional, and scripting languages.",
        "Open-source software is software that is released with its source code, allowing anyone to view, modify, and distribute it.",
        "Version control is a system that records changes to files, allowing multiple users to collaborate and track project history.",
        "A stack is a data structure that follows Last In First Out (LIFO), while a queue follows First In First Out (FIFO).",
        "Artificial intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.",
        "A hash table is a data structure that implements an associative array, allowing for efficient data retrieval.",
        "A variable is a storage location identified by a name that can contain data that may change during program execution.",
        "Loops are constructs that repeat a block of code as long as a specified condition is true.",
        "Multithreading allows multiple threads to run concurrently within a single process to optimize resource use and increase program efficiency.",
        "A bug is an error or flaw in software that causes it to produce incorrect or unexpected results.",
        "The main components of a computer include the CPU, memory (RAM), storage, input devices, and output devices.",
        "A network is a collection of computers and devices interconnected for sharing resources.",
        "RAM (Random Access Memory) is temporary storage for data in use, while ROM (Read-Only Memory) is permanent storage for firmware.",
        "A software framework is a platform for developing software applications, providing a foundation that includes predefined code.",
        "A web server is software or hardware that accepts requests from clients and serves web content.",
        "Encryption is the process of converting data into a coded format to prevent unauthorized access.",
        "Basic principles of software engineering include requirements analysis, design, implementation, testing, and maintenance.",
        "Debugging is the process of identifying and removing errors or bugs in a computer program or system.",
        "Front-end development focuses on the client side and user interface, while back-end development involves server-side and database management.",
        "A content management system (CMS) is a software application for creating, editing, and managing digital content.",
        "Data mining involves analyzing large datasets to discover patterns and extract useful information.",
        "Cloud storage allows users to store data on remote servers accessed over the internet.",
        "A software library is a collection of precompiled routines that a program can use.",
        "IPv4 addresses are 32 bits long, while IPv6 addresses are 128 bits long, allowing for a larger address space.",
        "A pixel is the smallest unit of a digital image, representing one point in a graphic.",
        "DNS (Domain Name System) translates human-readable domain names to IP addresses.",
        "Machine learning involves algorithms that learn from data to improve performance, while deep learning uses neural networks for more complex data.",
        "A computer network is a group of interconnected computing devices that can communicate and share resources.",
        "Blockchain technology is a decentralized digital ledger that securely records transactions across multiple computers.",
        "Algorithms optimize processes by making them more efficient and effective.",
        "HTTP (HyperText Transfer Protocol) transmits data over the web while HTTPS adds a layer of security (encryption).",
        "Chatbots are AI-driven tools designed to simulate conversation with users via text or voice.",
        "Gamification incorporates game design elements in non-gaming contexts to enhance user engagement.",
        "A macro is a sequence of instructions that can be triggered automatically to perform repetitive tasks in programming.",
        "A user interface (UI) is the point of interaction between a user and a computer or software application.",
        "An operating system is software that manages hardware resources and provides services for computer programs.",
        "Recursion involves functions calling themselves, while iteration involves repeating code through loops.",
        "The ethical implications of computer science include privacy, cybersecurity, and the impact of automation on employment.",
        "Careers in computer science include software developer, data scientist, systems analyst, and cybersecurity specialist.",
        "A neural network is a series of algorithms that mimic the human brain's interconnected neuron structure to recognize patterns.",
        "Augmented reality (AR) overlays digital information in the real world through devices.",
        "Virtual reality (VR) immerses users in a completely digital environment.",
        "Quantum computing uses quantum bits (qubits) to perform complex calculations faster than classical computers.",
        "The Turing machine is a hypothetical computation device that defines algorithmic computation.",
        "Data visualization refers to the graphical representation of information and data.",
        "A data warehouse is a centralized repository for storing large volumes of structured data for analysis.",
        "Cloud computing allows users to store, process, and access data over the internet, reducing dependency on local hardware and enabling scalable solutions.",
        "A mechanical computer uses mechanical components like gears and levers to perform calculations.",
        "The Analytical Engine, designed by Charles Babbage in the 1830s, was a mechanical general-purpose computer.",
        "Ada Lovelace is recognized as the first computer programmer for writing algorithms for the Analytical Engine.",
        "ENIAC was the first general-purpose electronic computer, developed in 1945.",
        "ENIAC was designed to calculate artillery firing tables for the U.S. Army during World War II.",
        "Vacuum tubes control the flow of electricity and were used in the first-generation computers.",
        "Transistors replaced vacuum tubes, making computers smaller, faster, and more reliable.",
        "Integrated circuits are small chips with many transistors, reducing size and cost in computers.",
        "A microprocessor acts as the CPU of a computer and was introduced in the fourth generation.",
        "The first microprocessor, the Intel 4004, was invented in 1971.",
        "The IBM PC, introduced in 1981, set industry standards for hardware and software.",
        "Moore's Law states the number of transistors on a microchip doubles every two years.",
        "The first programming language, Assembly, was developed in the 1940s.",
        "FORTRAN, short for Formula Translation, was an early high-level programming language.",
        "COBOL, or Common Business-Oriented Language, was developed for business applications in 1959.",
        "The World Wide Web was invented by Tim Berners-Lee in 1989 at CERN.",
        "The first computer virus, 'Creeper,' was created in the early 1970s.",
        "ARPANET, developed in the 1960s, was the precursor to the modern internet.",
        "UNIX, developed in 1969, influenced many modern operating systems like Linux and macOS.",
        "The Altair 8800, introduced in 1975, is considered the first personal computer.",
        "Apple introduced personal computing to the masses with the Apple II and Macintosh.",
        "A GUI allows users to interact with computers using visual elements like icons and windows.",
        "The Turing Machine, conceptualized by Alan Turing, laid the foundation for modern computing.",
        "Binary code uses 0s and 1s to represent data for processing by computers.",
        "The Von Neumann architecture describes a computer where data and instructions share the same memory.",
        "Punch cards were used in early computers for data input and storage.",
        "The first laptop, the Osborne 1, was invented in 1981.",
        "Microsoft developed MS-DOS and Windows, dominating personal computer operating systems.",
        "Computer networking began with ARPANET in the 1960s and evolved into the internet.",
        "Analog computers process continuous data, while digital computers use discrete binary data.",
        "Mainframe computers handle bulk data processing for large organizations.",
        "Linux is an open-source operating system introduced in 1991 by Linus Torvalds.",
        "Cloud computing provides remote access to resources like storage and software over the internet.",
        "Supercomputers emerged in the 1960s for tasks like weather forecasting and scientific research.",
        "Quantum computing uses quantum mechanics principles for complex computations.",
        "AI enables computers to perform tasks requiring human intelligence, like decision-making.",
        "The Macintosh introduced a GUI and mouse, revolutionizing personal computing in 1984.",
        "Supercomputers are designed for tasks requiring immense processing power, like simulations.",
        "Python, created in 1991, is a versatile language used in web development and AI.",
        "Java allows cross-platform applications with its 'write once, run anywhere' philosophy.",
        "Alan Turing contributed to theoretical computing, AI, and codebreaking during WWII.",
        "Punch cards were invented for storing data and programming early machines.",
        "Minicomputers brought computing to medium-sized businesses at lower costs.",
        "The Intel 8080 powered early personal computers and inspired software innovation.",
        "A compiler translates entire code at once, while an interpreter executes line by line.",
        "BASIC helped popularize personal computers by making programming accessible.",
        "Hard drives evolved from bulky devices in the 1950s to today's high-capacity SSDs.",
        "Wearable computers integrate technology into body-worn devices like smartwatches.",
        "PDAs were handheld devices for managing personal information, popular in the 1990s.",
        "Virtual memory extends RAM by using disk space for temporary data storage.",
        "Servers provide data and resources to clients over a network.",
        "Database systems evolved from hierarchical models in the 1960s to relational models in the 1970s.",
        "Vannevar Bush conceptualized the 'Memex,' an early idea for linked information systems.",
        "ROM stores permanent data, while RAM temporarily stores data during processing.",
        "The Macintosh 128K was Apple's first mass-market computer with a GUI.",
        "Video games started with experiments like 'Tennis for Two' and became a global industry.",
        "The Babbage Difference Engine was an early mechanical calculator.",
        "AI began in the 1950s and grew with advancements in machine learning and robotics.",
        "ASCII art uses characters from the ASCII standard to create images.",
        "Boolean logic forms the foundation of binary operations in computing.",
        "Computer vision enables machines to interpret visual data from images or videos.",
        "The Commodore 64 was a best-selling personal computer in the 1980s.",
        "GPUs evolved from rendering video game graphics to supporting AI and computations.",
        "Packet switching allows data to be sent in independent packets over a network.",
        "Email was first implemented in the 1970s using the ARPANET.",
        "Open-source software democratized development and innovation globally.",
        "USB standardized connections between computers and peripherals in the 1990s.",
        "IoT connects devices to the internet for communication and automation.",
        "Edge computing processes data closer to its source, reducing latency.",
        "Wearable technology integrates computing into everyday objects.",
        "Open-source software began with early collaborative projects like UNIX and flourished with Linux and GitHub, fostering a global development community.",
        "The history of computers spans centuries, beginning with early mechanical devices like the abacus, evolving to modern electronic machines capable of complex tasks.",
        "Key pioneers include Charles Babbage, Ada Lovelace, Alan Turing, Grace Hopper, and John von Neumann, among others.",
        "Computers are categorized into five generations based on technology: vacuum tubes, transistors, integrated circuits, microprocessors, and artificial intelligence.",
        "Computers are designed to process data, perform calculations, and execute tasks based on user input or programmed instructions.",
        "Early computers were used for calculations, such as solving equations, breaking codes, and automating repetitive tasks like census data processing.",
        "Computing has transformed industries, improved communication, enabled automation, and revolutionized fields like education, healthcare, and entertainment.",
        "Major milestones include the invention of the Analytical Engine, the creation of the ENIAC, the development of the internet, and the rise of personal computing.",
        "The internet revolutionized computing by connecting devices globally, enabling instant communication, and creating platforms for data sharing and innovation.",
        "Programming evolved from mechanical instructions to assembly language, followed by high-level languages like FORTRAN, C, and modern languages like Python.",
        "Key developments include the transition from vacuum tubes to transistors, the creation of integrated circuits, and advances in storage and processing power.",
        "World War II accelerated the development of computers for tasks like codebreaking and ballistics calculations, leading to innovations like the Colossus and ENIAC.",
        "Analog computers process continuous data, while digital computers use discrete binary data, allowing for more precise and versatile operations.",
        "Open-source software democratized computing by enabling collaboration, innovation, and free access to software like Linux and Apache.",
        "Computers became more accessible through innovations like personal computers, smartphones, and user-friendly interfaces, making them integral to daily life.",
        "AI represents a major milestone, enabling computers to perform tasks like speech recognition, image analysis, and decision-making, mimicking human intelligence.",
        "Universities like MIT, Stanford, and Cambridge have been hubs for computer science research, producing breakthroughs in algorithms, hardware, and software.",
        "Early business uses included automating payroll, managing inventory, and processing financial transactions, which streamlined operations and reduced costs.",
        "Mobile computing revolutionized accessibility, allowing people to use devices like smartphones and tablets for work, communication, and entertainment anywhere.",
        "Human-computer interaction evolved from punch cards to graphical user interfaces, touchscreens, and voice recognition, improving usability and accessibility.",
        "Cloud computing allows users to store, process, and access data over the internet, reducing dependency on local hardware and enabling scalable solutions."

    ]
}

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)
print("Dataset saved as 'dataset.csv'")