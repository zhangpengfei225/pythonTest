/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findTilt(TreeNode* root) {
        if (root == NULL) return 0;
        int rootTilt = abs(sumTilt(root->left) - sumTilt(root->right));
        return rootTilt + findTilt(root->left) + findTilt(root->right);       
    }
    //求一棵树的所有节点之和,相当于遍历整棵树
    int sumTilt(TreeNode* root){
        if (root == NULL) return 0;
        return root->val + sumTilt(root->left) + sumTilt(root->right);
    }
    
};
