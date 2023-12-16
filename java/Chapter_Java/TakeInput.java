/*
 * ==============================================
 *         🌟 Welcome to Java Chronicles 🌟
 * ==============================================
 *
 * 🚀 Chapter: Java
 *    Page: Takke User Input
 * 📅 Date: Wednesday || December 13, 2023 || Winter
 * 📖 Description: Taking User input.
 *
 * ----------------------------------------------
 *                 📜 Introduction 📜
 * ----------------------------------------------
 * ----------------------------------------------
 *            💡 Learning Objectives 💡
 * ----------------------------------------------
 * 1. Master the basics of Java syntax
 * 2. Build a solid foundation in OOP principles
 * 3. Explore advanced Java concepts
 *
 * ----------------------------------------------
 *             🚀 Let the Coding Begin! 🚀
 * ----------------------------------------------
 */

/**
 * Class: TakingUserInput
 *
 * 
 */

import java.util.Scanner;

class TakingUserInput {

    public static void main(String[] args) {
        // Code begins with greetings
        System.out.println("Hello, Java World!");
        // Taking input  from User

        Scanner name = new Scanner(System.in);

        Sysem.out.println("Hi user,\nTell me your name below?\n");
	String input = name.nextLine();

	System.out.println("Awesome!\nThanks for sharing your name, "+name+"\nMind sharing your age below?\n");
	Scanner age = new Scanner(System.in);
	int age = age.nextLine()    
}

}
