import java.util.Scanner;
public class questionEleven{
public static void main(String...args){

		Scanner scanner = new Scanner(System.in);
		
		double gallons = 1;
		
		
		while(gallons != 0){
		
		System.out.print("Enter gallons used or enter 0 to end: ");
		 gallons = scanner.nextInt();
		 
		 if (gallons != 0){
		
		System.out.print("Enter miles driven: ");
		double miles = scanner.nextInt();
		
		double milesPerGallon = miles / gallons;
			System.out.printf("The miles / gallons for this tank was %f%n ",milesPerGallon );
		   }
		   
		  else 
			System.out.print("Thank you. Hope to see you once again.");
		  
		
		}
	}

}