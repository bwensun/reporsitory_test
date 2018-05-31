timer测试代码：
    public static void main(String[] args) {
        System.out.println("测试timer开始");
        Timer timer = new Timer();
        TimerTest timerTest = new TimerTest();
        timer.schedule(timerTest, new Date());
        TimerTask timerTask2 = new TimerTask() {
            /**
             * The action to be performed by this timer task.
             */
            @Override
            public void run() {
                System.out.println(0);
            }
        };
        TimerTask timerTask3 = time2();
        timer.schedule(timerTask2,new Date(), 1000);
        timer.schedule(timerTask3,new Date(), 1000);

    }

    /**
     * The action to be performed by this timer task.
     */
    @Override
    public void run() {
        //logger.info("执行。。。");
        System.out.println("执行。。。");
    }

    @Test
    public void test1(){
        Timer timer = new Timer();
        TimerTest timerTest = new TimerTest();
        timer.schedule(timerTest, new Date(), 2000);
    }


    public static TimerTask time2(){
        return new TimerTask(){

            /**
             * The action to be performed by this timer task.
             */
            @Override
            public void run() {
                System.out.println("........");
            }
        };
    }
