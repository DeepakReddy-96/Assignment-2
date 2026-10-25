package Assignment_2;
/* Develop a Swing application that demonstrates at least three different event types (ActionEvent,
 MouseEvent, KeyEvent and ItemEvent) together with menus, and display the details of every event 
 received in a JTextArea.  */

// B6.java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class B6 {
    private static int clickCount = 0;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Multi-Event Mini Application");
            frame.setSize(700, 500);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLayout(new BorderLayout());

            JTextArea logArea = new JTextArea();
            logArea.setEditable(true);
            JScrollPane scrollLog = new JScrollPane(logArea);

            JToolBar toolBar = new JToolBar();
            JButton btnStart = new JButton("Start");
            JButton btnPause = new JButton("Pause");
            JButton btnStop = new JButton("Stop");

            toolBar.add(btnStart);
            toolBar.add(btnPause);
            toolBar.add(btnStop);

            JLabel statusLabel = new JLabel(" Typed Text: | Word Count: 0");

            ActionListener buttonListener = e -> {
                clickCount++;
                String cmd = e.getActionCommand();
                logArea.append("ActionEvent: " + cmd + " clicked (Count = " + clickCount + ")\n");
            };

            btnStart.addActionListener(buttonListener);
            btnPause.addActionListener(buttonListener);
            btnStop.addActionListener(buttonListener);

            logArea.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    logArea.append("MouseEvent: Clicked at (" + e.getX() + ", " + e.getY() +
                            ") with button" + e.getButton() + ", Clicks: " + e.getClickCount() + "\n");
                }

                @Override
                public void mousePressed(MouseEvent e) {
                    showPopup(e);
                }

                @Override
                public void mouseReleased(MouseEvent e) {
                    showPopup(e);
                }

                private void showPopup(MouseEvent e) {
                    if (e.isPopupTrigger()) {
                        JPopupMenu popup = new JPopupMenu();
                        JMenuItem itemClear = new JMenuItem("Clear Log");
                        JMenuItem itemCopy = new JMenuItem("Copy");

                        itemClear.addActionListener(ev -> logArea.setText(""));
                        itemCopy.addActionListener(ev -> logArea.copy());

                        popup.add(itemClear);
                        popup.add(itemCopy);
                        popup.show(e.getComponent(), e.getX(), e.getY());
                    }
                }
            });

            logArea.addMouseMotionListener(new MouseAdapter() {
                @Override
                public void mouseDragged(MouseEvent e) {
                    logArea.append("MouseEvent: Dragged at (" + e.getX() + ", " + e.getY() + ")\n");
                }
            });

            StringBuilder typedText = new StringBuilder();
            logArea.addKeyListener(new KeyAdapter() {
                @Override
                public void keyTyped(KeyEvent e) {
                    char ch = e.getKeyChar();
                    if (!Character.isISOControl(ch)) {
                        typedText.append(ch);
                    }
                    String text = typedText.toString().trim();
                    int wordCount = text.isEmpty() ? 0 : text.split("\\s+").length;
                    statusLabel.setText(" Typed Text: " + typedText.toString() + " | Word Count: " + wordCount);
                    logArea.append("KeyEvent: Typed '" + ch + "' (code=" + (int) ch + ")\n");
                }

                @Override
                public void keyPressed(KeyEvent e) {
                    logArea.append("KeyEvent: Pressed key code " + e.getKeyCode() + " (" + KeyEvent.getKeyText(e.getKeyCode()) + ")\n");
                }

                @Override
                public void keyReleased(KeyEvent e) {
                    logArea.append("KeyEvent: Released key code " + e.getKeyCode() + " (" + KeyEvent.getKeyText(e.getKeyCode()) + ")\n");
                }
            });

            JMenuBar menuBar = new JMenuBar();
            JMenu menuFile = new JMenu("File");
            JMenuItem itemNew = new JMenuItem("New");
            JMenuItem itemExit = new JMenuItem("Exit");
            itemExit.addActionListener(e -> frame.dispose());
            menuFile.add(itemNew);
            menuFile.add(itemExit);

            JMenu menuEdit = new JMenu("Edit");
            JCheckBoxMenuItem itemEditable = new JCheckBoxMenuItem("Editable", true);
            itemEditable.addItemListener(e -> {
                boolean editable = itemEditable.isSelected();
                logArea.setEditable(editable);
                logArea.append("ItemEvent: Editable checked = " + editable + "\n");
            });

            JRadioButtonMenuItem rbSmall = new JRadioButtonMenuItem("Small");
            JRadioButtonMenuItem rbLarge = new JRadioButtonMenuItem("Large");
            ButtonGroup fontGroup = new ButtonGroup();
            fontGroup.add(rbSmall);
            fontGroup.add(rbLarge);

            ItemListener fontListener = e -> {
                if (rbSmall.isSelected()) {
                    logArea.setFont(new Font("Monospaced", Font.PLAIN, 12));
                } else if (rbLarge.isSelected()) {
                    logArea.setFont(new Font("Monospaced", Font.PLAIN, 18));
                }
                logArea.append("ItemEvent: Font size changed\n");
            };

            rbSmall.addItemListener(fontListener);
            rbLarge.addItemListener(fontListener);

            menuEdit.add(itemEditable);
            menuEdit.addSeparator();
            menuEdit.add(rbSmall);
            menuEdit.add(rbLarge);

            JMenu menuHelp = new JMenu("Help");

            menuBar.add(menuFile);
            menuBar.add(menuEdit);
            menuBar.add(menuHelp);

            frame.setJMenuBar(menuBar);
            frame.add(toolBar, BorderLayout.NORTH);
            frame.add(scrollLog, BorderLayout.CENTER);
            frame.add(statusLabel, BorderLayout.SOUTH);

            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}
