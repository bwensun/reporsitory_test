package com.yogovi.core.common;

import lombok.*;

/**
 * 常量
 *
 * @author bowensun
 * @since 2018/6/20
 */
public interface Constant {
    /**
     * 微信模板ID
     *
     */
    @AllArgsConstructor
    enum TemplatedId implements Constant{
        /** 审核通知微信模板ID **/
        approveWechatTemplateId("ru_YmjNWbyK2nhJBAQbOv4rv3Ye64Kq1Y3HqcjqRIds"),
        ;
        @Getter
        private String id;
    }

    /**
     * 导出excel表格列名
     *
     */
    @AllArgsConstructor
    enum Excelexport implements Constant{
        /** 导出发货单 **/
        deliveryInfoFieldNames(new String[]{"payTime", "deliveryCode", "receiverName", "productName", "productNum", "productUnit",
                "transFee", "liftSelf", "receiverProvince", "receiverCity", "receiverArea", "receiverName",
                "receiverPhone", "receiverStreet", "ReceiveAddress", "expressComName", "expressCodes"}),;
        @Getter
        private String[] fieldNames;
    }


}
