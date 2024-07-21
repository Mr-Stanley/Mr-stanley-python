import java.util.Scanner;
public class questionSixteen{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);
	
	int largest = 0;
	int secondLargest = 0;
	int userInput = 0;
	
		
	for(int number = 1; number <= 4; number++){
		System.out.print("Enter number: ");
		 userInput = scanner.nextInt();
		
		if (userInput > largest) {
			secondLargest = largest;
			largest = userInput;
		}
		else if (userInput < largest && userInput > secondLargest){
			secondLargest = userInput;
		}
				
		}
		System.out.printf("The largest number is %d%n", largest);
		System.out.printf("The second largest is %d", secondLargest);
	
	
	



}



}