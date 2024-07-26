package jpabook.jpashop.domain;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@Builder
public class UpdateItemDto {

    private String name;
    private int price;
    private int stockQuantity;
}
