public class Complex 
{
    public Complex() 
	{
        this(0);
    }

    public Complex(double r) 
	{
        this(r, 1);
    }

    public Complex(double r, double j) 
	{
        this.r = r;
        this.j = j;
    }

    public Complex add(Complex o) 
	{
		return new Complex(o.r + r, o.j + j);
    }

    public Complex add(double n) 
	{
        return new Complex(n + r, j);
    }
    
    public Complex add(double n, Complex o)
    {
    	return new Complex(n + o.r, o.j);
    }

    public Complex div(Complex o) 
	{
        return new Complex((o.r * r + o.j * j) / (o.r*o.r + o.j*o.j), (o.r * j - o.j * r) / (o.r*o.r + o.j*o.j));
    }

    public Complex div(double n) 
	{
        return new Complex(r / n, j / n);
    }
    
    public Complex div(double n, Complex o)
    {
    	return new Complex(n / o.r, 0 / o.r);
    }

    public Complex mul(Complex o) 
	{
        return new Complex(((o.r * r) - (o.j * j)), ((o.j * r) + (o.r * j)));
    }

    public Complex mul(double n) 
	{
        return new Complex(n * r, n * j);
    }
    
   	public Complex mul(double n, Complex o)
   	{
   		return new Complex(n * o.r, n * o.j);
   	}

    public Complex sub(Complex o) 
	{
        return new Complex(r - o.r, j - o.j);
    }

    public Complex sub(double n) 
	{
        return new Complex(r - n, j);
    }
    
    public Complex sub(double n, Complex o)
    {
    	return new Complex(n - o.r, 0 - o.j);
    }

    public String toString() 
	{
        return "(" + r + ") + (" + j + ")i";
    }
    
    private double j;
    private double r;
}
