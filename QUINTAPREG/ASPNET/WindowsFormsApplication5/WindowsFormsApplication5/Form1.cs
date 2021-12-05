using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string pos = textBox1.Text;
            int c = 1;
            int a = 0;
            int b = 1;
            for (int i = 2; i <= Convert.ToInt32(pos); i++)
            {
                c = a + b;
                a = b;
                b = c;
            }
            label2.Text = c + "";
        }
    }
}
