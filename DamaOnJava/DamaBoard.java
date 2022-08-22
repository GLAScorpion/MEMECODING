import java.util.Arrays;

public class DamaBoard {
    private DamaPedina[][] board = new DamaPedina[8][8];
    private int whitePlayer=0;
    private int blackPlayer=0;
    DamaBoard(){
        fillBoard();
    }
    private void addPawn(boolean clr){
        if(clr){
            whitePlayer++;
        }else{
            blackPlayer++;
        }
    }
    private void subPawn(boolean clr){
        if(clr){
            whitePlayer--;
        }else{
            blackPlayer--;
        }
    }
    private int ydirCalc(int dir){
        if(dir == 0 || dir== 3 ) return -1;
        return 1;
    }
    private int xdirCalc(int dir){
        if(dir == 3 || dir== 2 ) return -1;
        return 1;
    }
    public int checkNextMove(int xOrigin, int yOrigin){//XXXX == 0 1 2 3
        int result=0;
        DamaBoard tmp = new DamaBoard();
        System.arraycopy(board, 0, tmp.board, 0, 8);
        boolean colorOrigin = tmp.board[yOrigin][xOrigin].getColor();
        boolean damaOrigin = tmp.board[yOrigin][xOrigin].isDama();
        if(colorOrigin || damaOrigin){
            if(move(xOrigin,yOrigin,0) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result += 1000;
                tmp.subPawn(colorOrigin);
            }
            if(move(xOrigin,yOrigin,3) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result += 1;
                tmp.subPawn(colorOrigin);
            }
        }
        if(!colorOrigin || damaOrigin){
            if(move(xOrigin,yOrigin,1) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result += 100;
                tmp.subPawn(colorOrigin);
            }
            if(move(xOrigin,yOrigin,2) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result += 10;
                tmp.subPawn(colorOrigin);
            }
        }
        return result;
    }
    public boolean move(int xOrigin, int yOrigin, int dir){
        /*
          3 = \   / = 0
                O
          2 = /   \ = 1
        */ 
        int x = xOrigin + xdirCalc(dir); 
        int y = yOrigin + ydirCalc(dir);
        boolean colorOrigin = board[yOrigin][xOrigin].getColor();
        boolean damaOrigin = board[yOrigin][xOrigin].isDama();
        try{
            boolean colorEnd = board[y][x].getColor();
            boolean damaEnd = board[y][x].isDama();
            if(colorOrigin == colorEnd || (!damaOrigin && damaEnd)){
                return false;
            }
            x += xdirCalc(dir); 
            y += ydirCalc(dir);
            if(board[y][x]==null){
                board[y][x] = board[yOrigin][xOrigin];
                board[yOrigin][xOrigin] = null;
                addPawn(colorOrigin);
                return true;
            }
            return false;
        }
        catch(NullPointerException e){
            board[y][x] = board[yOrigin][xOrigin];
            board[yOrigin][xOrigin] = null;
            return true;
        }
        catch(IndexOutOfBoundsException e){
            return false;
        }

    }
    public int whoWon(){
        int black = 0;
        int white = 0;
        boolean tmp = false;
        for(int a = 0; a < 8; a++){
            for(int b = 0; b < 8; b++){
                try{
                    tmp = board[a][b].getColor();
                    if(tmp){
                        white++;
                    }else{
                        black++;
                    }
                }
                catch(NullPointerException e){
                }
            }
        }
        if(black == 0){
            return 1;
        }else if(white == 0){
            return 0;
        }else{
            return -1;
        }
    }
    public String toString(){
        String s = "";
        boolean tmp = false;
        for(int a = 0; a < 8; a++){
            for(int b = 0; b < 8; b++){
                try{
                    tmp = board[a][b].getColor();
                    if(tmp){
                        s += "w ";
                    }else{
                        s += "b ";
                    }
                }
                catch(NullPointerException e){
                    s += "X ";
                }
            }
            s+= "\n";
        }
        return s;
    }
    private void fillBoard(){
        for(int a=0; a < 3; a++){
            for (int b = 0; b < 4; b++) {
                board[a][b*2 + a%2] = new DamaPedina(false);
            }
        }
        for(int a=5; a < 8; a++){
            for (int b = 0; b < 4; b++) {
                board[a][b*2 + a%2] = new DamaPedina(true);
            }
        }
    }
}
