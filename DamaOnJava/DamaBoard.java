public class DamaBoard {
    private DamaPedina[][] board = new DamaPedina[8][8];
    private int whitePlayer=0;
    private int blackPlayer=0;
    DamaBoard(){
        fillBoard();
    }
    public int getPlayer(boolean clr){
        if(clr){
            return whitePlayer;
        }
        return blackPlayer;
    }
    public boolean isOwner(int xOrigin, int yOrigin, boolean clr){
        return board[yOrigin][xOrigin].getColor() == clr;
    }
    public boolean canMove(int xOrigin, int yOrigin){
        boolean[] tmp = checkNextMove(xOrigin, yOrigin);
        return tmp[0] || tmp[1] || tmp[2] || tmp[3];
    }
    public boolean canNextEat(int xOrigin, int yOrigin){
        boolean[] tmp = checkNextEat(xOrigin, yOrigin);
        return tmp[0] || tmp[1] || tmp[2] || tmp[3];
    }
    public void boardPromote(boolean clr){
        int index = 0;
        if(clr){
            index = 7;
        }
        for(int a = 0; a < 8; a++){
            try{
                if(board[index][a].getColor()==clr){
                    board[index][a].promote();
                }
            }
            catch(NullPointerException e){/*left empty*/}
        }
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
    public static int ydirCalc(int dir){
        if(dir == 0 || dir== 3 ) return -1;
        return 1;
    }
    public static int xdirCalc(int dir){
        if(dir == 3 || dir== 2 ) return -1;
        return 1;
    }
    public boolean[] checkNextMove(int xOrigin, int yOrigin){
        boolean[] result = new boolean[4];
        DamaBoard tmp = new DamaBoard();
        System.arraycopy(board, 0, tmp.board, 0, 8);
        boolean colorOrigin = tmp.board[yOrigin][xOrigin].getColor();
        boolean damaOrigin = tmp.board[yOrigin][xOrigin].isDama();
        if(colorOrigin || damaOrigin){
            if(move(xOrigin,yOrigin,0)){
                result[0] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
                tmp.subPawn(colorOrigin);
            }
            if(move(xOrigin,yOrigin,3)){
                result[3] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
                tmp.subPawn(colorOrigin);
            }
        }
        if(!colorOrigin || damaOrigin){
            if(move(xOrigin,yOrigin,1)){
                result[1] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
                tmp.subPawn(colorOrigin);
            }
            if(move(xOrigin,yOrigin,2)){
                result[2] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
                tmp.subPawn(colorOrigin);
            }
        }
        return result;
    }
    public boolean[] checkNextEat(int xOrigin, int yOrigin){//XXXX == 0 1 2 3
        boolean[] result=new boolean[4];
        DamaBoard tmp = new DamaBoard();
        System.arraycopy(board, 0, tmp.board, 0, 8);
        boolean colorOrigin = tmp.board[yOrigin][xOrigin].getColor();
        boolean damaOrigin = tmp.board[yOrigin][xOrigin].isDama();
        if(colorOrigin || damaOrigin){
            if(move(xOrigin,yOrigin,0) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result[0] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
                tmp.subPawn(colorOrigin);
            }
            if(move(xOrigin,yOrigin,3) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result[3] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
                tmp.subPawn(colorOrigin);
            }
        }
        if(!colorOrigin || damaOrigin){
            if(move(xOrigin,yOrigin,1) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result[1] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
                tmp.subPawn(colorOrigin);
            }
            if(move(xOrigin,yOrigin,2) && (tmp.blackPlayer == 1 || tmp.whitePlayer==1)){
                result[2] = true;
                tmp.board[yOrigin][xOrigin] = new DamaPedina(colorOrigin, damaOrigin);
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
                board[yOrigin + ydirCalc(dir)][xOrigin + xdirCalc(dir)] = null;
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
    public boolean anyMoves(boolean clr){
        boolean[] tmp = new boolean[4];
        for(int a = 0; a<8; a++){
            for(int b = 0; b < 8; b++ ){
                try{
                    tmp = this.checkNextMove(b, a);
                }
                catch(NullPointerException e){/* left empty */}
                if(tmp[0] || tmp[1] || tmp[2] || tmp[3]){
                    return true;
                }
            }
        }
        return false;
    }
    public int whoWon(){
        if(!anyMoves(true)){
            return 0;
        }
        if(!anyMoves(false)){
            return 1;
        }
        return -1;
    }
    public String toString(){
        String s = "";
        for(int a = 0; a < 8; a++){
            for(int b = 0; b < 8; b++){
                try{
                    if(board[a][b].getColor() && !board[a][b].isDama()){
                        s += "w ";
                    }else if(!board[a][b].isDama()){
                        s += "b ";
                    }else if(board[a][b].getColor()){
                        s += "W ";
                    }else{
                        s += "B ";
                    }
                }
                catch(NullPointerException e){
                    if((a + b + 1)%2==0){
                        s += "  ";
                    }else{
                        s += "■ ";
                    }
                }
            }
            s+= "\n";
        }
        return s;
    }
    private void fillBoard(){
        for(int a=1; a <= 3; a++){
            for (int b = 0; b < 4; b++) {
                board[a-1][b*2 + a%2] = new DamaPedina(false);
            }
        }
        for(int a=6; a <= 8; a++){
            for (int b = 0; b < 4; b++) {
                board[a-1][b*2 + a%2] = new DamaPedina(true);
            }
        }
    }
}
