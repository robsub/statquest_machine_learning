# statquest_machine_learning

one branch - main

1) check sizes (very large upload to colab times out)

for file in *.png; do echo "$file:"; sips -g pixelWidth -g pixelHeight "$file"; echo ""; done


2) reduce sizes

for file in *.png; do sips -Z 300 "$file"; done


3) upload to colab

4) push notebook to github 

TO DO:
BRANCHES

In_progress: Use this branch for your ongoing work on the tutorial, creating commits as you complete each
section or chapter.

Finished_don't_understand: Use this branch to track sections or chapters that you have completed but don't
fully understand yet. You can return to this branch later to review and improve your understanding.

Finished_understand_most: Use this branch for sections or chapters that you have completed and understand
for the most part, but may need to revisit later.

Finished_understand_completely: Use this branch for sections or chapters that you have completed and fully
understand.

Revised: Use this branch for revisions or improvements to your code and understanding of the tutorial.

Expert: Use this branch for advanced topics or applications of the tutorial that go beyond the basic
material covered in the tutorial.
