DIR=$1
VALIDPCT=$2
if [ -z $VALIDPCT ]; then
    VALIDPCT=20
fi

mkdir $DIR/valid
mkdir $DIR/train
mkdir $DIR/sample
mkdir $DIR/sample/valid
mkdir $DIR/sample/train

for class in $(ls $DIR); do
    if [ "$class" != "valid" -a "$class" != "train" -a "$class" != "sample" ]; then
        # This is a real class

        # Copy up to 100 images into the sample validation and train sets
        for typ in valid train; do
            mkdir $DIR/sample/$typ/$class
            for f in $(ls $DIR/$class | shuf | head -n 100); do
                cp $DIR/$class/$f $DIR/sample/$typ/$class/$f;
            done
        done

        # Create the real validation set
        mkdir $DIR/valid/$class
        num_files=$(ls $DIR/$class | wc -l)
        num_valid_files=$(echo "$num_files * $VALIDPCT/100.0" | bc)
        for f in $(ls $DIR/$class | shuf | head -n $num_valid_files); do
            mv $DIR/$class/$f $DIR/valid/$class/$f;
        done

        # Move the rest into the training set
        mkdir $DIR/train/$class
        mv $DIR/$class/* $DIR/train/$class/

        # Remove the old directory
        rmdir $DIR/$class
    fi
done
