import java.util.Scanner;
public class questionSix{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);
	String correct = "yes";
	String incorrect = "no";
	
	System.out.print("What is your problem: ");
	String problem = scanner.nextLine();
	
	System.out.print("Have you had this problem before (yes or no): ");
	String respond = scanner.nextLine();
	

	if (respond.equals (correct)){
		System.out.print("Well you have it again.");
		}
	else if (respond.equals (incorrect) ){
		System.out.print("Well, you have it now");
	}
	else 
		System.out.print("Invalid input");

}

}