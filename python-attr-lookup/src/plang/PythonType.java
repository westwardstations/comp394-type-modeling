package plang;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * A Python class.
 */
public class PythonType extends PythonObject {

    private final String name;
    private final PythonObject base;

    /**
     * Declares a new Python type. Equivalent to Python `class «name»(«base»):`
     * @param name The name of this class.
     * @param base The base class of this class. May be null.
     *             (In real Python, instead of null it would be the class called `object`, and
     *             it would be a list instead of a single value.)
     */
    public PythonType(String name, PythonObject base) {
        super(null);  // In real Python, this would be the type called `type`
        this.name = name;
        this.base = base;
    }

    /**
     * The name of this class.
     */
    public String getName() {
        return name;
    }

    /**
     * The base type (superclass) of this class.
     */
    public PythonObject getBase() {
        return base;
    }

    @Override
    protected List<PythonObject> buildMRO() {
        ArrayList mroList = new ArrayList<PythonObject>();
        mroList.add(this);
        if(this.getBase() != null) {
            mroList.add(this.getBase());
            return mroList;
        }
        return Collections.singletonList(this);
    }


    /**
     * Creates and returns a new instance of this class, i.e. a PythonObject whose type is
     * this PythonType.
     */
    public PythonObject instantiate() {
        return new PythonObject(this);
    }

    @Override
    public String toString() {
        return "PythonType<" + name + ">";
    }
}
