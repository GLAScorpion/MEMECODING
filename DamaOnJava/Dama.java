import java.util.*;
public class Dama{
    public static void main(String[] args){
        DamaBoard dama = new DamaBoard();
        boolean player = true;
        Scanner s = new Scanner(System.in);
        int x = 0, y = 0;
        do{
            System.out.println(dama.toString());
            System.out.println("Coordinate pedina. (x y, partendo da 0)");
            boolean insertCicle;
            do{
                insertCicle = true;
                try{
                    x = s.nextInt();
                    y = s.nextInt();
                    if(x > 7 && y > 7 && x < 0 && y < 0){
                        System.out.println("Inserisci valori in range. Riprova");    
                    }else if(!dama.isOwner(x, y, player)){
                        System.out.println("Non è la tua pedina. Riprova");  
                    }else if(!dama.canMove(x, y)){
                        System.out.println("Pedina immobile, scegline un'altra");                      
                    }else{
                        insertCicle = false;
                    }
                }
                catch(InputMismatchException e){
                    System.out.println("Errore. Inserisci valori numerici");
                    s.nextLine();
                }
                catch(NullPointerException e){
                    System.out.println("Spazio vuoto. Riprova");
                }
            }while(insertCicle);
            boolean[] tmp = dama.checkNextMove(x, y);
            int choice = chooseDir(tmp);
            int previusPlayer = dama.getPlayer(player);
            if(!dama.move(x, y, choice)){
                throw new UnknownError();
            }
            if(previusPlayer < dama.getPlayer(player)){
                boolean eatCicle = true; 
                do {
                    x += DamaBoard.xdirCalc(choice) * 2; 
                    y += DamaBoard.ydirCalc(choice) * 2;
                    tmp = dama.checkNextEat(x, y);
                    if(tmp[0] || tmp[1] || tmp[2] || tmp[3]){
                        choice = chooseDir(tmp);
                        dama.move(x, y, choice);
                    }else{
                        eatCicle = false;
                    }
                } while (eatCicle);
            }
            dama.boardPromote(player);
            int winCond = dama.whoWon();
            if(winCond == 1){
                System.out.println("Giocatore di razza superiore ha vinto.");
                break;
            }
            if(winCond == 0){
                System.out.println("Giocatore di razza inferiore ha rotto i coglioni.");
                break;
            }
            System.out.println("\033[H\033[2J");
            if(player){
                player = false;
            }else{
                player = true;
            }
            
        }while(true);
        s.close();
    }
    private static int chooseDir(boolean[] tmp){
        Scanner s = new Scanner(System.in);
        System.out.println("Scegli direzione ()");
            if(tmp[0]){
                System.out.print("(0) up dx\t");
            } if(tmp[1]){
                System.out.print("(1) down dx\t");
            } if(tmp[2]){
                System.out.print("(2) down sx\t");
            } if(tmp[3]){
                System.out.print("(3) up sx\t");
            }
            System.out.println();
            int choice = -1;
            do {
                try{
                    choice = s.nextInt();
                    if(!tmp[choice]){
                        System.out.println("Inserisci valori in range. Riprova");    
                    }else{
                        s.close();
                        return choice;
                    }
                }
                catch(InputMismatchException e){
                    System.out.println("Errore. Inserisci valori numerici");
                    s.nextLine();
                }
                catch(ArrayIndexOutOfBoundsException e){
                    System.out.println("Inserisci valori in range. Riprova");
                }
            } while (true);
    }
}