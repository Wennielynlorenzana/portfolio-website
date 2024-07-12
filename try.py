I take a BS Information Technology in college, and Being a Software Developer is to 
            manage and create a simple project and be able to contribute to a more complex 
            as my first time career. Self-motivated and adaptable developer with applicable database knowledge 
            and coding skills by organized programmer by looking for an opportunity.


font-size: 1.6rem;
  margin: 2rem 0 3rem;

about me

This one of my interest in doing what I like, how to fix my own code
            I have focused on developing my skill and ability.
            I enjoy working on my own projects independently.
            I'm excited to use my skill when I want to do my job as a developer.
            I want to experience other things. I would like to see my proficieny 
            in the technical aspects of my work. The highlight of my career is 
            to gain more knowledge, learn everyday and to improve myself.



services

github -    It is a web-based interface that uses Git, 
                        the open source version control software that 
                        lets multiple people make separate changes to 
                        web pages at the same time.

AI -    AI is the biggest machine learning 
                        that people use, ability of computer-controlled 
                        robot to perform tasks that intellectual 
                        processes characteristic of humans

algorithms -    A method of organizing data in a virtual system. 
                        both well-defined data structures. An algorithm is 
                        a sequence of steps executed by a computer 
                        that takes input and transforms into target output.

SQL -   A relational databases, 
                        systems that store collections of tables 
                        and organize structured sets of data in a 
                        tabular columns-and-rows format, similar 
                        to that spreadsheet.

.text-animation {
  font-size: 34px;
  font-weight: 600;
  min-width: 280px;
}
.text-animation span{
  position: relative;
}
.text-animation span::before {
  content: 'Software Developer';
  color: var(--main-color);
  animation: words 20s infinite;
}
.text-animation span::after {
  content: '';
  background-color: var(--bg-color);
  position: absolute;
  width: calc(100% + 8px);
  height: 100%;
  border-left: 3px solid #f1f1f1;
  right: -8px;
  animation: cursor 0.6s infinite, typing 20s steps(14) infinite;
}
@keyframes cursor {
  to {
    border-left: 2px solid var(--main-color);
  }
}

@keyframes words {
  0%, 20% {
    content: 'Software Developer';
  }
}
@keyframes typing{
  10%,
  15%,
  30%,
  35%,
  50%,
  55%,
  70%,
  75%,
  90%,
  95%{
      width: 0;
  }
  5%,
  20%,
  25%,
  40%,
  45%,
  60%,
  65%,
  80%,
  85%{
      width: calc(100% + 8px);
  }
}