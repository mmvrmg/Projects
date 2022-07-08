import java.util.Scanner;


public class parkingCharges{
    public static String inputString(String message){
        Scanner scanner = new Scanner(System.in);
        String answer;
        System.out.println(message);
        answer = scanner.nextLine();
        return answer;
    } 

    public static String isDisabled(){
        String disabled = inputString("Are you disabled? (yes or no)");
        return disabled;
    }

    public static int totalHours(){
        int hours = inputString("How long would you like to park for? (1-8)");
        return hours;
    }

    public static String hasBadge(){
        String badge = inputString("Do you have an 'I live locally' badge? (yes or no)");
        return badge;
    }

    public static String isOAP(){
        String oap = inputString("Are you an OAP?");
        return oap;
    }

    public static int calculateCharge(int hours,){
        int chargeAmount;
        if (hours == 1){
            chargeAmount = 3;
        }
        elif (hours<=4); and (hours>=2);{
            chargeAmount = 4;
        }
        elif (hours<=6); and (hours>=5);{
            chargeAmount = 4.50;
        }
        elif (hours<=8); and (hours>=7);{
            chargeAmount = 5.50;
        }
        //fill in the rest of if statements for each hour bracket
    }

    public static void main(String args[]){
        if 
    }
}