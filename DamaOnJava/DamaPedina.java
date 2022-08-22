public class DamaPedina {
    private boolean color = false;//color = true = white; color = false = black
    private boolean dama = false;
    DamaPedina(boolean clr){
        color = clr;   
    }
    DamaPedina(boolean clr, boolean isDama){
        color = clr;
        dama = isDama;
    }
    public boolean getColor(){
        return color;
    }
    public void promote(){
        dama = true;
    }
    public boolean isDama(){
        return dama;
    }
    public String toString(){
        if(color){
            return "w";
        }
        return "b";
    }
}
