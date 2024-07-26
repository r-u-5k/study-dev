package jpabook.jpashop.domain.item;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UpdateItemDto {

    private String name;
    private int price;
    private int stockQuantity;
}
